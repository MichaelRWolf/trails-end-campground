# Raw Rambling -- Registration Process Case Study

This file captures unedited observations, stories, metaphors, and framework dimensions for the LinkedIn article. Preserved in original form--stream-of-consciousness, incomplete terminology, working thoughts--to be reorganized and polished into article prose later.

## Context & Framing

I hope to assume Aaron would be receptive to a proposal to change the registration process if I provided an adequate analysis of why the new system improves one aspect but severely degrades another. Wendy's coaching is that we are not invited for that. I understand that. I also want to believe that somebody who doesn't know something about how his customers are being harmed in his vision would want to hear about it. A middleway is to look at this as a professional posting on LinkedIn that shows an aspect of system design, then second-purpose it to Aaron.

So much has been floating around in my head that I need to get it out.

---

## Three Critical Attributes: Comparison Framework

Comparing the old process and the new process for three critical attributes:

- Capacity guaranteed
- Payment
- Site selection

### Old System (Arrival-Time, On-Site)

The original system was like a murmuration, or traffic, because it allowed individual site selection at the moment of selection. Everything happens at once. Upon arrival. Arrive. Determine if there was availability. Select a site. Make payment. Approximately the same time. In any order. But for these purposes, at the same time which we will call arrival time.

The problem here is that if there is no vacancy, people have no other options and have invested a lot to get here--hours or days. This is in theory, but in practice it could be a large risk that prevented people from showing up.

### New System (Planning-Time, Off-Site)

The online system provides capacity checking before arrival. This gives people peace of mind and a guaranteed entrance. The new online system provides this peace of mind--alleviating anxiety over risking a no-vacancies situation at arrival with limited other options and a huge investment in time and money. Peace of mind. That's the phrase.

In order to provide this vacancy guarantee, an online system was selected that allowed people to reserve space. But let's get terminology consistent here: reserving space (campground-wide capacity limit) versus reserving a space (selecting a specific site). I think that by trying to provide a capacity guarantee with an online system, the terms got conflated and the system does both. In fact, it moved all three actions (vacancy guarantee, payment, site selection) from arrival time in person on-site, to planning time off-site. Since the system had features for all three, it was easy to move all three from arrival time to planning time.

This solves the problem of not knowing vacancy until arrival, but it created another problem.

---

## The Three Stories

### 1. Jan and Her Dog

Before arrival, Jan selected a site online and paid. Upon arriving, she noticed an electric fence adjacent to her site that would be a problem for her dog. She saw many vacant sites nearby, but did not know how to switch sites. She walked up front, read the board, connected to Wi-Fi, pulled up the app to see what sites would be available if she registered now, walked back to see if any would work, then back to the front to see if she could switch sites with the app. I saw her and connected her with Stener, who had the admin privileges to modify the reservation in the database. Some of the sites that were vacant were not available due to site selection locking for future arrivals.

**Under the old system:** After noticing that the selected site was not appropriate, she could have selected any other site that was vacant and moved there without inviting time to modify a reservation. Vacant == Available. Self-serve. But under the old system, she would not have been locked into the inappropriate site. What's more, she never would have been forced to select a site that was inappropriate for her. She's simply show up and select a site, instead of changing a site.

### 2. Steven & Friends

Steven did online/offsite registration. He noted "The site is sunnier than we expected." He would have preferred one of the shadier sites that were vacant, but did not know how to make the switch. He decided to enjoy the area rather than invest time switching online or finding someone who could do that for him. In essence, he sweated it out.

**Under the old system:** Upon arrival they never would have locked themselves into the sunny site. Rather, they would have simply set up in a shady site. Without the database blocking selection, he makes a selection based on the terrain, not the map (i.e. database).

### 3. Kevin in a Hammock

Kevin did not register offsite. Instead, he just showed up, remembering the process from previous years. He drove around taking pictures of vacant sites then went to the front to see which vacant sites were available. The system timed out while registering, but somehow had placed a hold on that site so he had to go with his #2 choice.

**Under the old system:** Kevin drives around, finds the site that feels right, walks to the front, and registers it. No timeout, no provisional hold, no second-best compromise.

### Analysis of All Three Cases

In all 3 cases, the previous site selection process would have worked.

Can you process shift all three of those to offsite pre-arrival time? Anytime before arriving, do all three online? No--that's the problem. You can't do site selection well before arriving. Not without losing something essential.

---

## Alternative Stories: Self-Service Outcomes

In the current system, all three stories required staff intervention or frustration due to database limitations. Here's how they would look under a system that preserves on-site autonomy:

### 1. Jan and Her Dog (Self-Service Version)

Jan arrives and walks the campground with her dog. She notices that a couple of sites have electric fences nearby and avoids those. She finds a perfect site--open enough for her dog to roam safely, shaded, quiet, near water. She walks to the office, confirms it's available, registers it, pays, and sets up.

**Outcome:** Jan gets the right site for her needs. Zero staff time spent on modification. She feels trusted and respected. She feels smart--she made a good decision based on direct observation.

### 2. Steven & Friends (Self-Service Version)

Steven and friends arrive and spend 30 minutes walking the campground together, discussing what they want. "We'd prefer shade." They find a shady spot with great views. Someone says "this one feels right." They walk to the office, confirm availability, register, pay, and set up.

**Outcome:** Steven's group makes a collaborative decision. They got their preferred site. Zero staff time. The site selection process itself was part of the bonding experience--learning about each other's preferences, moving around the landscape together. The decision is not a regretted compromise, but a shared win.

### 3. Kevin in a Hammock (Self-Service Version)

Kevin arrives, remembering the simple process from before. He drives around, takes pictures of vacant sites, finds one with a perfect tree for his hammock and a good view. He walks to the office, registers it, pays, sets up.

**Outcome:** Kevin is in control. No timeouts, no provisional holds, no second-best compromise. He selected exactly the site that matched his (admittedly specific) needs. Zero staff time. He feels competent and autonomous.

---

### The Self-Service Pattern

In all three alternative versions:

- **No database permission required** -- camper sees it's vacant, it's available
- **No staff intervention** -- the decision and action are self-serve
- **No frustration** -- camper gets what they wanted, without bureaucratic friction
- **No staff time spent** -- registration, switching, adjustments all happen without admin help
- **Trust signaled** -- the system says "we trust you to make good choices"

The cost of on-site autonomy is low. The benefit is substantial: freedom, agency, correct outcomes, and a hospitality message that says "we respect your ability to know what's good for you."

---

## Metaphors

### The Map Is Not the Terrain

The terrain clearly shows occupied/vacant sites in present time. The map (i.e. database) is a model of the site, but adds a dimension of time that complicates present-time selection. Sites that are vacant may not (according to the DB) be available. This is non-obvious to the person on-site and therefore requires an app, and likely a person. The database has restricted choices based on criteria that do not exist in the field at the present time.

### Murmuration

Starlings murmurate--thousands of birds moving together in complex, flowing patterns. It looks like complex flock-level behavior, but it is actually the cumulative effect of bird-level, simple choices. (Align direction and speed roughly the same as 2-4 local neighbors, avoid collisions). No bird sees the whole system. The system does not control a bird. The bird controls itself. The system does not collide. This is how interstate traffic works. This is how the site selection used to work.

Every newly arrived camper selected a site based on their own perspective. No central control was needed. Everyone got the best site available at the time. People had ground truth--sun, shade, space, views, proximity. They used their real human senses to observe sun, shade, weather, wind, smells, sounds and real human feelings to know if the site felt right.

### Different Chairs (Christopher Alexander)

Allowing people to select a chair that fits them sends a welcoming message. Requiring everyone to sit in identical chairs sends a requirement for conformity, fitting in, and devalues personal preferences and expression. Does the chair serve you, or do you serve the system?

**The Stinger:**

If this were a KOA, where every site is as identical as a Motel 6 room, it would be OK to select a site from a dropdown list. This campground is much richer than that. Denying campers the luxury, freedom, and autonomy is denying them the richness that was created here.

Requiring "permission" from a database before occupying a site deprives them of a sense of freedom that was previously present. Coupling site selection to a database requires staff intervention for the kinds of actions that were previously self-serve: site selection, switching sites, extending visit duration.

Having to find a staff member is not only a time investment and frustration in bureaucracy, it is also a signal--of distrust, lack of respect, and reduced hospitality. Conversely, self-service signals trust. It signals "we trust you to make good choices for yourself."

---

## Terminology & Distinctions

### Deciding vs. Decision

- **Decision** -- what site is ultimately chosen
- **Deciding** -- during the deciding process, who has input, and what input is available

### Information Available

**For site selection:**

- Offsite: The only info available online is a site number, and a stylized map.
- In-person: People can use their human senses to observe sun, shade, weather, wind, how the site feels.

**For CG capacity:**

- In-person: Count the vacant sites now.

### Time Concepts

- **Arrival time:** the instant a camper arrives at the campground
- **Planning time:** before arrival, while at home or on the road
- **Capacity commitment time:** when does the CG commit capacity to the camper?
- **Site commitment time:** when does the camper commit to the site?

Maybe the concept should be "Campground Commitment" and "Site Commitment" instead of Capacity Guarantee and Site selection. Yeah. It's really about when a decision is committed. Until then, it is provisional. When does the CG commit capacity to the camper? When does the camper commit to the site?

### Visibility Attributes

- **Capacity** is a collective attribute, visible at the campground level. Dependent on all sites, collectively.
- **Site availability** is an individual activity. Independent of other sites.

### Vacant vs. Available

With the older system: if a site was vacant, it was available for selection.

With the newer system: a site must be vacant, but it can be unavailable for non-now reasons.

### Locking and Blocking

I like the terms lock-in or block regarding someone locking (in CS terminology, not for general consumption) a resource but not actively utilizing it. I have a vested interest in painting locking, blocking, and lock-in as bad choices that remove freedom.

---

## General Guidelines

- Make choices that maximize future options and choices
- Blocking a site IS OK if you are on it now. Not so much if you are not.
- A site that is locked/blocked but not used is a wasted resource
- Do not make choices that unnecessarily limit future options and choices.
- Maximize freedom. (Maybe freedom is another way to say options and choices.)
- Maximize autonomy. Let people make decisions regarding their own experience based on their personal preferences.
- Local decisions based on local observations.
- Allow maximum choices now.
- Prefer choices of someone on-site over someone off-site.
- Prefer choices for now versus future
- There is not an "optimal" or rigid selection criteria. Most campers have a continuum of preferences. If #1 is taken, #2 is likely OK. There is abundance of choices and variations. There are only a few cases that exclude a camper from being satisfied with any site (e.g. solar power dies in the shade, large vehicles can't fit in some sites). Beyond those, it's mostly a continuum of preferences (e.g. prefer to be close-to or distant-from bathrooms).

---

## The Campground's Variety (Zinger Material)

The campground has an amazing variety of sites. This is something neutral for the LinkedIn article, but powerful if Aaron reads it and reflects on what we're constraining by forcing pre-selection:

- Sun: morning, evening, mid-day, all-day, none
- Open feel, cozy feel
- Lake view, mountain view, lake + mountain view
- Orchard view, farm view
- Connected to other sites for groups
- Isolated from all sites
- Easy pull-through
- Plant your tent on a hill like a castle

---

## System Analysis: Original vs. New

### Original System: Two Near-Optimal, One Fragile

**Site selection:**

- Great. Near optimal. Probably as good as a CS algorithm could get.
- Needs only local knowledge by the camper.
- Appropriate coupling to: present campers, personal preferences, sensory input.
- Appropriate decoupling to: non-present campers, future campers (or no-shows).

**Payment:**

- Great show of values--trust and laid-back vibe.

**Availability:**

- PROBLEM. NO VACANCY signal arrives too late.
- Lack of guarantee prevents folks from investing travel time.

### New System: Trades Off--Solves Availability, Breaks Site Selection

**Availability:**

- Optimal. Guarantees "general admission" as early as camper wants.
- Can be at arrival on-site, or any time before that while off-site.

**Payment:**

- Appropriate. Camper commits money when campground commits general admission.
- Could be deferred until arrival, but that is asymmetric commitment and more difficult logistics.

**Site selection:**

- Inappropriate coupling: present vs. absent inverted priority. Now versus future (or no-show) inverted priority. Invisible coupling of occupied versus available.
- Inappropriately frames offsite selection as a "promise or commitment" which is better framed as an inappropriately forced decision with inadequate information.
- Locking site selection before arrival blocks choices for onsite campers.
- Dissociating vacant-is-identical-to-available visual indicator (think Kanban) requires a database to mediate site selection.
- That requires an app. And WiFi (flakey and only available at welcome board, not at sites).
- Cannot run app at the site. Must return to hotspot.
- Cannot simultaneously view site and also view availability. Can see that site is vacant, but cannot lookup if site is available.
- This violates "You have arrived. Turn off your phone" message from tourist information brochure.
- Violates Copper Harbor vibe of "No Cell Service" and the joy that comes from unplugging.
- Most importantly, requiring site selection without full sensory and feeling denies one of the joys of site selection at this campground.
- When people "go away" for a destination campground like this, one of the joys is to wander around with your fellow campers to make a joint decision for where to live and how to live together.
- This involves conversations. Learning about each other's preferences. Collaborative decision making.
- And the joy of knowing that you have selected the best site for all of you based on numerous criteria, none of which can be conveyed on a dropdown list--what does it look like? What does it feel like? Can I be happy here? Does it feel safe here?
- All those criteria that a deer has in the woods before laying down for the night.
- These decisions should be made on site. In the moment.
- There is so much variety here! That is one of the joys of this place.
- Denying people the luxury of imagining how they want to live while on vacation.... Well, that's disheartening.
- And it denies the wealth of possibilities, and all the love and attention that went into creating such a wonderful variety of choices.

---

## Key Dimensions: Decision-Process Framework

The decision to come to the campground is actually three separate decisions, each with its own dimensions:

### Dimension 1: TIMING (When is the decision made?)

| Decision                 | Old System         | New System                 |
|--------------------------|--------------------|----------------------------|
| **Campground Guarantee** | Checked at arrival | Guaranteed before arrival  |
| **Payment Commitment**   | At arrival         | Before arrival             |
| **Site Selection**       | At arrival         | Before arrival (locked in) |

**Key insight:** Timing affects information availability. At arrival, campers can see/feel the sites. Before arrival, they can only see a map and description. These are very different information sets.

### Dimension 2: INFORMATION SOURCE (What info is available?)

| Context                       | Campground Guarantee                   | Payment | Site Selection                                                     |
|-------------------------------|----------------------------------------|---------|--------------------------------------------------------------------|
| **Off-site (before arrival)** | Database query (current state)         | N/A     | Map, description, site number                                      |
| **On-site (at arrival)**      | Visual count (current state + sensory) | N/A     | Visual observation + sensory input (sun, shade, views, wind, vibe) |

**Key insight:** On-site information is exponentially richer for site selection. Off-site information is sufficient for checking general capacity.

### Dimension 3: DECISION MAKER (Who chooses?)

| Decision                 | Who Decides            | Authority                                       | Staff Role                       |
|--------------------------|------------------------|-------------------------------------------------|----------------------------------|
| **Campground Guarantee** | Campground (system)    | Institutional                                   | Runs availability database       |
| **Payment**              | Camper (with CG rules) | Mixed                                           | Process transaction              |
| **Site Selection (old)** | Camper                 | Individual                                      | Confirms availability, processes |
| **Site Selection (new)** | Camper (off-site)      | Individual (but constrained by future bookings) | Constrained by database rules    |

**Key insight:** The new system takes individual site selection and subordinates it to institutional constraints (future bookings, database locks). The old system honored individual judgment at the moment of arrival.

### Dimension 4: REVERSIBILITY (Can the decision be changed?)

| Decision                 | Old System                           | New System                                        |
|--------------------------|--------------------------------------|---------------------------------------------------|
| **Campground Guarantee** | Check at arrival; if full, send away | Decided before arrival; binding                   |
| **Payment**              | At arrival; reversible if leaving    | Before arrival; reversible but requires app/staff |
| **Site Selection**       | At arrival; self-serve site switch   | Before arrival; requires app or staff help        |

**Key insight:** Early commitment removes flexibility. The new system locks people in before they have full information.

### Dimension 5: SELF-SERVICE vs. STAFF-MEDIATED

| Decision           | Old System                                 | New System                                    |
|--------------------|--------------------------------------------|-----------------------------------------------|
| **Site Selection** | Self-serve (see it, claim it)              | Staff-mediated (requires app or person)       |
| **Site Switching** | Self-serve (move to vacant site)           | Staff-mediated (requires database mod or app) |
| **Stay Extension** | Self-serve (add more time, update payment) | Staff-mediated (requires database mod)        |

**Key insight:** Moving decisions to a database backend transforms what used to be self-serve autonomy into staff-dependent requests.

---

## Lexicon: Standard Terms

To avoid conflating different concepts, use these terms precisely:

### Campground-Level Decisions

- **Capacity Check / Campground Guarantee** -- Is there room for this camper at the campground (any site)? This is a binary yes/no about general admission.
- **Availability Guarantee** -- The camper has confirmed peace of mind that they can come; the CG commits to having a site for them.

### Site-Level Decisions

- **Site Vacancy** -- Is the physical site currently unoccupied? (Observable on-site; shown on a map as "unoccupied")
- **Site Availability (in database)** -- Does the database rules permit selecting this site? (May differ from vacancy due to locks, holds, future bookings)
- **Site Selection** -- The camper chooses which specific site they will occupy.

### Critical Distinction

**"Guaranteeing Capacity" does NOT require "Pre-assigning Specific Sites."**

- Old system: Capacity is NOT guaranteed; site selection is autonomous (on-site).
- New system: Capacity IS guaranteed; site selection is pre-assigned (off-site, locked in).
- Alternative system: Capacity could be guaranteed while site selection remains autonomous (on-site).

### Commitment Types

- **Camper Commitment to Campground** -- "I'm coming; I've paid; I have a guaranteed spot"
- **Camper Commitment to Specific Site** -- "I'm coming to *this site*; it's mine"

These are separable. You can have one without the other.

---

## Heuristics for Decision Placement

Based on the analysis, use these heuristics to decide WHEN and WHERE decisions should be made:

### Heuristic 1: "Value Presence Over Off-Site"

When full sensory and contextual information is important, push the decision to the moment of presence (on-site, in-person) over off-site planning.

**Applies to:** Site selection. Visual observation, feeling, spatial awareness, collaboration with travel companions--all improve on-site. Off-site you have maps; on-site you have ground truth.

**Applies to:** Stay duration (how long do we want to be here?). Better decided after a day or two, not weeks before.

### Heuristic 2: "ASAP for Guarantees, Delay for Refinements"

Move guarantees as early as possible (so campers can plan). Delay refinements until full information is available.

**Applies to:** Capacity guarantee should be early (off-site, as soon as camper wants to plan). Site selection should be late (on-site, with full information).

### Heuristic 3: "Maximize Autonomy and Self-Service"

Avoid requiring staff intervention for decisions that can be made independently by the camper.

**Applies to:** Site selection, switching, duration changes. When a camper can see a vacant site and claim it themselves, they should be able to. No database required; no staff required; trust the camper.

### Heuristic 4: "Prefer Reversible Decisions"

When committing early, ensure the decision can be easily changed if circumstances change.

**Applies to:** Site selection. If locked in before arrival, make it trivial to switch once on-site (one conversation, no app, no database lookup).

### Heuristic 5: "Signal Trust Through Self-Service"

Systems that say "we trust you to make good choices" build better relationships than systems that say "you need permission from the database."

**Applies to:** Letting campers select their own sites. Not just the functional outcome, but the *signal* matters. "We respect your judgment" is different from "we control your options."

---

## Open Questions

- What is best terminology about collective campground vacancy, capacity, availability?
- What is best terminology about specific sites? Vacant. Available. Occupied (by me, by someone else). Unavailable.
- Could the campground guarantee capacity while preserving on-site site selection?
- What would a "hybrid" system look like that moved only the capacity guarantee off-site, while keeping site selection at arrival?
