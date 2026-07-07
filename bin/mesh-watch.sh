#!/bin/bash

# mesh-watch.sh — Real-time display of all visible Trails End mesh APs and signal strength
# Shows which AP you're currently connected to, helps visualize roaming
# Usage: ./mesh-watch.sh [interval_seconds]

INTERVAL="${1:-2}"
AIRPORT_CMD="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"

while true; do
  clear
  echo "═══════════════════════════════════════════════════════"
  echo "Trails End Mesh Monitor — $(date '+%H:%M:%S')"
  echo "═══════════════════════════════════════════════════════"
  echo ""

  # Current connection info
  current_info=$("$AIRPORT_CMD" -I 2>/dev/null)
  current_ssid=$(echo "$current_info" | grep "SSID:" | sed 's/.*SSID: *//')
  current_bssid=$(echo "$current_info" | grep "BSSID:" | sed 's/.*BSSID: *//' | sed 's/[[:space:]]*$//')
  current_signal=$(echo "$current_info" | grep "agrCtlRSSI:" | sed 's/.*: *//')

  if [ -z "$current_bssid" ] || [ "$current_bssid" = "BSSID:" ]; then
    echo "CONNECTED: $current_ssid (not connected or signal unavailable)"
  else
    echo "CONNECTED: $current_ssid @ $current_bssid | Signal: $current_signal dBm"
  fi

  echo ""
  echo "All visible Trails End APs (strongest at top):"
  echo "──────────────────────────────────────────────────────"
  echo "Signal  BSSID             SSID"
  echo "──────────────────────────────────────────────────────"

  # Parse airport -s output
  # Format is usually: [spaces]SSID[spaces]BSSID[spaces]RSSI[other fields]
  # Extract by finding BSSID pattern (MAC address) and working backwards for SSID
  $AIRPORT_CMD -s 2>/dev/null | grep -E "Trails End" | while read -r line; do
    # Use awk to find BSSID (MAC pattern) and extract signal/SSID
    echo "$line" | awk '{
      bssid=""
      signal=""
      for(i=1; i<=NF; i++) {
        # Look for BSSID pattern (XX:XX:XX:XX:XX:XX)
        if($i ~ /^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$/) {
          bssid=$i
          signal=$(i+1)
          # Everything before BSSID is SSID
          ssid=""
          for(j=1; j<i; j++) {
            if(j>1) ssid=ssid" "
            ssid=ssid$j
          }
          break
        }
      }
      if(bssid=="") {
        # Fallback: if no BSSID found, check if line contains what looks like signal and extract that way
        for(i=NF; i>=1; i--) {
          if($i ~ /^-[0-9]+$/) {
            signal=$i
            break
          }
        }
        ssid=$1" "$2" "$3
      }
      if(bssid != "" && signal != "") {
        printf "%-7s %-17s %s\n", signal, bssid, ssid
      }
    }'
  done | sort -rn

  echo ""
  echo "Update: ${INTERVAL}s | Press Ctrl+C to exit"
  sleep "$INTERVAL"
done
