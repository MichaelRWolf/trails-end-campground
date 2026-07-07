#!/bin/bash

# ubiquiti-ap-scan.sh — Scan visible Ubiquiti APs and their signal strength
# Usage: ./ubiquiti-ap-scan.sh [output_file]
# Helps map BSSID → AP location for correlation with speedtest results

OUTPUT_FILE="${1:-speedtest-logs/ubiquiti-ap-map.txt}"
LOGDIR="$(dirname "$0")/../speedtest-logs"

mkdir -p "$LOGDIR"

echo "========================================"
echo "Ubiquiti AP Scanner"
echo "========================================"
echo "Scanning visible APs and their signal strength..."
echo ""

# Get available SSIDs and their BSSIDs/signal
airport_scan=$(/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s 2>/dev/null)

# Filter for "Trails" networks (adjust if needed)
echo "Visible Trails End Wifi APs:"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')" | tee -a "$OUTPUT_FILE"
echo "" | tee -a "$OUTPUT_FILE"
echo "SSID                           BSSID             Signal Channel" | tee -a "$OUTPUT_FILE"
echo "──────────────────────────────────────────────────────────────" | tee -a "$OUTPUT_FILE"

echo "$airport_scan" | grep -E "Trails End" | awk '{
  for(i=1; i<=NF; i++) {
    if($i ~ /^([0-9a-f]{2}:){5}[0-9a-f]{2}$/) {
      bssid=$i
      signal=$(i+1)
      ssid=""
      for(j=1; j<i; j++) {
        if(j>1) ssid=ssid" "
        ssid=ssid$j
      }
      printf "%-30s %-17s %s\n", ssid, bssid, signal
      break
    }
  }
}' | tee -a "$OUTPUT_FILE"

echo "" | tee -a "$OUTPUT_FILE"
echo "To map these to physical AP locations:"
echo "1. Document BSSID for each AP location (note which building/zone each AP serves)"
echo "2. Refer to this BSSID in speedtest logs to identify which antenna tested from" | tee -a "$OUTPUT_FILE"
echo "   each location" | tee -a "$OUTPUT_FILE"
echo "" | tee -a "$OUTPUT_FILE"

echo "Appended to: $OUTPUT_FILE"
