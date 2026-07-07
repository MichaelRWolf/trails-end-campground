# Signal Mapping Guide -- Site 1 (July 7, 2026)

**Goal:** Map WiFi signal strength around Site 1 to present options to Stenar tomorrow.

**Constraint:** No cell service → manual GPS marking or grid-based approach.

---

## Approach 1: Manual Grid + Speedtest (Fastest for Today)

**Setup (5 min):**

1. Use existing Site 1 map (printed or phone camera)
2. Mark a ~50 ft grid around your RV location
3. Use MacBook + phone as mobile rig

**Walking Route (15-20 min total):**

- Start at RV center
- Walk to each grid corner + center
- Mark RSSI from WiFi menu + speedtest result

**Data Collection:**

```text
Grid: Site 1 area (approximate distances from RV)

        North
          |
    [NW] [N] [NE]
     50ft  50ft
    [W]  [RV] [E]
     50ft  50ft
    [SW] [S] [SE]
          |
        South

For each position:
- Note: direction + distance
- RSSI: WiFi network menu (-XX dBm)
- Speedtest: iperf3 or speedtest.net (30 sec)
```

**Minimal Data Sheet (fill as you walk):**

| Location   | RSSI (dBm) | Down (Mbps) | Up (Mbps) | Latency (ms) | Notes    |
|------------|------------|-------------|-----------|--------------|----------|
| RV (start) | -XX        | _           | _         | _            | baseline |
| North 50ft | -XX        | _           | _         | _            |          |
| East 50ft  | -XX        | _           | _         | _            |          |
| South 50ft | -XX        | _           | _         | _            |          |
| West 50ft  | -XX        | _           | _         | _            |          |
| NW corner  | -XX        | _           | _         | _            |          |
| NE corner  | -XX        | _           | _         | _            |          |

---

## Approach 2: RSSI-Only Map (2 min, Best for Quick Summary)

If speedtest takes too long, just walk the grid and collect RSSI + note antenna direction:

```text
From WiFi menu (macOS: ⌥ click WiFi icon):
  SSID: Trails End WiFi
  RSSI: -XX dBm (this number!)
  Channel: XX (2.4G or 5G)
  Signal Bars: XX
```

Plot on grid; color-code by signal strength:

- Green: -50 to -70 dBm (strong)
- Yellow: -70 to -80 dBm (usable)
- Red: <-80 dBm (weak)

---

## Approach 3: iPhone Automation (If You Have Time)

**Tools to try:**

1. **iStatistica** app (free): logs WiFi RSSI + GPS (if available) continuously
2. **Speedtest app** + Notes: manual logging, but faster than web speedtest
3. **iperf3** on MacBook: hardwire speedtest to specific location, log results

**Quick iPhone + MacBook Setup (10 min):**

```bash
# On MacBook, start iperf3 server at RV
iperf3 -s -p 5201

# Move around with iPhone, connect to WiFi
# From iPhone terminal (or MacBook at each location):
iperf3 -c <macbook-ip> -p 5201 -t 5 | tee speedtest.log

# Repeat at each grid location
```

---

## Tomorrow's Talking Points (Prep Now)

**From Today's Map:**

1. Signal strength at Site 1 vs barn area
2. Dead zones (if any)
3. Which SSID gives best performance (Trails End Wifi, Crew, or barn Starlink)
4. Hypothesis: registration antenna blocked by foliage or inactive

**Proposal to Stenar:**

- "I can help map full-campground signal, create coverage diagram"
- Offer: volunteer network assessment + optimization
- Request: either better service tier or co-working office arrangement
- Timeline: "I could have a full map in a few days"

**Key Questions to Ask:**

- Which antenna broadcasts which SSID?
- Is registration antenna active? Why weak signal at Site 1?
- Any planned network upgrades?
- Interest in having dedicated network volunteer?

---

## Tools in Your Repo

```bash
# From wolf-soho/Trails_End/bin/:
./uplink-short       # identify current uplink (Starlink vs Pasty)
./uplink-describe    # traceroute + uplink details
networkQuality -v    # responsiveness (RPM) + latency
```

**For Site 1:** mostly irrelevant (campus network, not WAN uplink), but good for baseline.

---

## Quick Reference: WiFi RSSI Scale

- **-30 dBm:** Excellent (right next to AP)
- **-50 to -60 dBm:** Very good (strong signal)
- **-70 dBm:** Good (usable, some interference)
- **-80 dBm:** Acceptable (usable, slower)
- **-90 dBm:** Weak (may disconnect)
- **<-100 dBm:** No signal

---

## Today's Timeline

- **2:00 PM:** First speedtest at RV (get baseline)
- **2:10-2:30 PM:** Walk grid, collect RSSI + speedtest
- **2:30-3:00 PM:** Compile map, prepare talking points
- **3:00 PM onward:** Rest; prep meeting slides/notes
- **Tomorrow, 2:00 PM (approx):** Pow wow meeting

**Goal:** Have signal map + 2-3 talking points ready for Stenar.
