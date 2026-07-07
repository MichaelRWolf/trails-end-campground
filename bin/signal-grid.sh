#!/bin/bash

# signal-grid.sh — Auto-logging RSSI grid survey (no interactive prompts)
# Usage:
#   ./signal-grid.sh                          # uses default Site 1 grid
#   ./signal-grid.sh "North 50ft" "East 50ft" # custom locations as args
#   ./signal-grid.sh --file location-list.txt # read locations from file

set -e

AIRPORT_CMD="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
LOGDIR="$(dirname "$0")/../speedtest-logs"
LOGFILE="$LOGDIR/$(date +%Y-%m-%d)-rssi-grid.csv"

mkdir -p "$LOGDIR"

# Create CSV header if file doesn't exist
if [ ! -f "$LOGFILE" ]; then
  echo "timestamp,location,ssid,bssid,signal_dbm,channel" > "$LOGFILE"
fi

# Default grid locations for Site 1
declare -a LOCATIONS=(
  "RV Center (baseline)"
  "North 50ft"
  "East 50ft"
  "South 50ft"
  "West 50ft"
  "NW Corner"
  "NE Corner"
  "SE Corner"
  "SW Corner"
)

# Parse command-line args
if [ $# -gt 0 ]; then
  if [ "$1" = "--file" ]; then
    # Read from file
    LOCATIONS=()
    while IFS= read -r line; do
      [ -z "$line" ] && continue
      LOCATIONS+=("$line")
    done < "$2"
  else
    # Use args as location list
    LOCATIONS=("$@")
  fi
fi

echo "========================================"
echo "RSSI Grid Survey — Trails End"
echo "========================================"
echo "Locations: ${#LOCATIONS[@]}"
echo "Output: $LOGFILE"
echo ""

count=0
for location in "${LOCATIONS[@]}"; do
  count=$((count + 1))
  echo "Scanning: $location"

  timestamp=$(date '+%Y-%m-%d %H:%M:%S')

  # Capture WiFi info (single airport call to reduce overhead)
  airport_info=$("$AIRPORT_CMD" -I 2>/dev/null)
  ssid=$(echo "$airport_info" | grep "SSID:" | head -1 | sed 's/.*SSID: *//' | tr -d '\n' | sed 's/[[:space:]]*$//')
  bssid=$(echo "$airport_info" | grep "BSSID:" | sed 's/.*BSSID: *//' | sed 's/[[:space:]]*$//')
  signal=$(echo "$airport_info" | grep "agrCtlRSSI:" | sed 's/.*: *//')
  channel=$(echo "$airport_info" | grep "channel:" | sed 's/.*: *//')

  # Validate capture
  if [ -z "$signal" ] || [ "$signal" = "0" ]; then
    echo "  ✗ No WiFi connection"
    continue
  fi

  # Log to CSV
  echo "$timestamp,$location,$ssid,$bssid,$signal,$channel" >> "$LOGFILE"

  echo "  ✓ Signal: $signal dBm | BSSID: $bssid | SSID: $ssid"

  # Pause between samples (allows moving to next location)
  if [ $count -lt ${#LOCATIONS[@]} ]; then
    sleep 2
  fi
done

echo ""
echo "========================================"
echo "✓ Survey complete!"
echo "Results: $LOGFILE"
echo ""
echo "View results:"
echo "  cat $LOGFILE"
echo "  column -t -s, $LOGFILE | less -S"
echo "========================================"
