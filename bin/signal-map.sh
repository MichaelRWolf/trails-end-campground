#!/bin/bash

# signal-map.sh — Auto-logging speedtest survey by location with antenna/AP tracking
# Usage: ./signal-map.sh
# Prompts for location name, runs 3 speedtests, logs results to CSV with BSSID/signal strength

set -e

LOGFILE="$(date +%Y-%m-%d)-signal-map.csv"
LOGDIR="$(dirname "$0")/../speedtest-logs"

mkdir -p "$LOGDIR"
LOGFILE="$LOGDIR/$LOGFILE"

# Create CSV header if file doesn't exist
if [ ! -f "$LOGFILE" ]; then
  echo "timestamp,location,ssid,bssid,signal_dbm,channel,down_mbps,up_mbps,latency_ms,jitter_ms" > "$LOGFILE"
fi

echo "========================================"
echo "Signal Map Logger — Trails End Site 1"
echo "========================================"
echo "Results saved to: $LOGFILE"
echo ""

location_count=0

while true; do
  echo ""
  read -p "Location name (or 'quit' to exit): " location

  if [ "$location" = "quit" ] || [ "$location" = "q" ]; then
    break
  fi

  if [ -z "$location" ]; then
    echo "Please enter a location name."
    continue
  fi

  location_count=$((location_count + 1))

  echo ""
  echo "Location $location_count: $location"
  echo "Running 3 speedtests..."
  echo ""

  test_num=0
  for i in 1 2 3; do
    echo "  Test $i/3..."

    # Capture WiFi info via airport command (text + XML for robustness)
    airport_text=$(/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I 2>/dev/null)
    ssid=$(echo "$airport_text" | grep "SSID:" | head -1 | sed 's/.*SSID: *//' | tr -d '\n' | sed 's/[[:space:]]*$//')
    bssid=$(echo "$airport_text" | grep "BSSID:" | sed 's/.*BSSID: *//' | sed 's/[[:space:]]*$//')

    # Parse signal strength via XML (more robust than text grep)
    airport_xml=$(/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I -x 2>/dev/null)
    if [ -n "$airport_xml" ]; then
      json_data=$(echo "$airport_xml" | plutil -convert json - -o - 2>/dev/null)
      signal=$(echo "$json_data" | jq -r '.RSSI_CTL_AGR // "null"' 2>/dev/null)
      channel=$(echo "$json_data" | jq -r '.CHANNEL // "null"' 2>/dev/null)
    else
      signal=""
      channel=""
    fi

    # Validate signal capture
    if [ -z "$signal" ] || [ "$signal" = "null" ] || [ "$signal" = "0" ] || ! [[ "$signal" =~ ^-?[0-9]+$ ]]; then
      echo "    ✗ No WiFi signal (parsing failed)"
      continue
    fi

    # Run speedtest with JSON output
    if result=$(speedtest --json 2>/dev/null); then
      timestamp=$(date '+%Y-%m-%d %H:%M:%S')

      # Parse JSON with jq (speedtest outputs in Mbps), handle nulls
      down_int=$(echo "$result" | jq -r '(.download // 0) | floor')
      up_int=$(echo "$result" | jq -r '(.upload // 0) | floor')
      ping_int=$(echo "$result" | jq -r '(.ping // 0) | floor')
      jitter_int=$(echo "$result" | jq -r '(.jitter // 0) | floor')

      # Log to CSV with BSSID and signal info
      echo "$timestamp,$location,$ssid,$bssid,$signal,$channel,$down_int,$up_int,$ping_int,$jitter_int" >> "$LOGFILE"

      echo "    ✓ Down: ${down_int} Mbps | Up: ${up_int} Mbps | Ping: ${ping_int} ms | Signal: ${signal} dBm | AP: ${bssid}"
      test_num=$((test_num + 1))
    else
      echo "    ✗ Speedtest failed (no internet or speedtest-cli error)"
    fi

    [ $i -lt 3 ] && sleep 10
  done

  if [ $test_num -gt 0 ]; then
    echo ""
    echo "✓ $test_num/3 tests completed at $location"
    echo "Move to next location (or 'quit' to finish)"
  else
    echo "✗ All tests failed at $location. Check connection and retry."
  fi
done

echo ""
echo ""
echo "========================================"
echo "Survey complete!"
echo "Results saved to: $LOGFILE"
echo ""
echo "To view results:"
echo "  cat $LOGFILE"
echo "  or open in spreadsheet app:"
echo "  open $LOGFILE"
echo ""
echo "BSSID column shows which Ubiquiti AP you're connected to."
echo "Create a mapping of BSSIDs to AP locations to identify antenna coverage."
echo "========================================"
