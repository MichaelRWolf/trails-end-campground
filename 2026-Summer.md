# Summer 2026 -- Site 1 Network Characterization

## Activity Log (newest on top)

### Monday, July 7 -- Site 1, Afternoon

**Location:** Site 1 (moved from barn area, <100 ft from registration station antenna)

**SSID:** Trails End Wifi (5G)

**Speedtest results:**

- Down: **Mbps | Up:** Mbps | Latency: **ms | Jitter:** ms
- *(enter results)*

**Observations:**

- Poor speeds inside RV despite proximity to antenna
- Unclear if registration antenna is active
- Uncertain which SSIDs use which antenna (Trails End Wifi, Trails End Crew, others?)
- Possible foliage issue: ~3-ft wide tree near front antenna at similar height
- Last year (Sept 2025): bucket-on-roof test showed better signal, suggesting foliage impact or barn-roof antenna path advantage

**Signal mapping plan:**

- Characterize signal around Site 1 today (semi-automated speedtest map)
- Prep talking points for tomorrow's pow wow meeting

---

## Pow Wow Meeting -- Tuesday, July 8

**Attendees:** Stenar (new CG manager), Aaron, Johnnie, Adrian, Kelsi

**Opportunity:** Present network map + request for improved service / become "chief network guy" role or co-working office agreement

**Talking points to prepare:**

- Signal mapping results from today
- Hypothesis: foliage blocking registration antenna or antenna inactive/misconfigured
- Proposal: volunteer network assessment/improvements in exchange for better service or co-working arrangement
- Tools needed: signal mapping app (iPhone/macbook semi-automated speedtest) to reduce manual grid walking

---

## Network Context (2026 Summer)

**Current Setup:**

- Barn roof: Starlink + Pasty.net dual uplink (per historical docs)
- Registration station antenna: likely 5G (Trails End Wifi, possibly others)
- Site 1: <100 ft from registration antenna, but signals weak indoors

**Known Unknowns:**

- Which SSIDs are on which antenna?
- Is registration antenna active/properly configured?
- Foliage impact on registration antenna path?
- Barn-roof vs registration-antenna coverage map?

**No longer available:**

- wolfden-mesh experiment (failed; removed)
- Cursor app (no longer relevant for testing)

---

## Resources

- Historical topology: `/Users/michael/repos/wolf-soho/network_rv.md`, `Trails_End/` docs
- Monitoring tools: `uplink-short`, `uplink-describe`, `uplink-monitor` in `wolf-soho/Trails_End/bin/`
- Signal mapping: currently manual speedtest grid; need semi-automated app
