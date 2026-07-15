# Standardized Terminology

This is the authoritative reference for terms used in the LinkedIn article and analysis. Includes standard terms, non-preferred alternatives, and why the distinction matters.

---

## Core Concepts (The Two Things That Got Coupled)

### REGISTRATION (The Bundle)

**Standard term:** REGISTRATION  
**What it is:** The two linked administrative actions: Capacity Commitment + Payment  
**Optimal timing:** Pre-arrival, offsite (ASAP)  
**Why "registration":** It's a single administrative act that makes sense to move together

**Non-preferred alternatives that caused confusion:**

- ❌ "Booking" (too vague; doesn't distinguish from site assignment)
- ❌ "Reservation" (implies site-specific, which it isn't)
- ❌ "General Admission" (sounds temporary; doesn't describe the payment action)
- ❌ "Online system" (too broad; describes technology, not the process)

---

### CAPACITY COMMITMENT (Part of Registration)

**Standard term:** CAPACITY COMMITMENT  
**What it is:** The campground's guarantee that an unoccupied site will be available upon the camper's arrival  
**Committer:** Campground system (makes the promise); Camper (accepts and pays)  
**Information needed:** Current occupancy + business rules  
**Optimal timing:** Pre-arrival, offsite, ASAP  
**Staff service required:** None (just confirmation)

**Non-preferred alternatives that caused confusion:**

- ❌ "Availability Guarantee" (sounds like it includes site assignment)
- ❌ "General Admission" (museum-like term; confuses the scope)
- ❌ "Vacancy Check" (sounds like arrival-time activity; happens too late for peace of mind)
- ❌ "Reserving a space" (implies a specific site; this is campground-wide)
- ❌ "Peace of Mind" (describes the benefit, not the mechanism)

**Why precision matters:** Conflating "Capacity Commitment" with "Site Selection" is the root of the coupling problem. Different timing needs. Different information. Different decision-maker.

---

### SITE SELECTION (The Decision)

**Standard term:** SITE SELECTION  
**What it is:** The individual camper choosing which specific unoccupied site they will occupy  
**Who decides:** Camper (individual)  
**Information needed:** Sensory observation (sun, shade, views, vibe, proximity, feel)  
**Optimal timing:** On-site, at arrival, with full sensory information  
**Staff service required:** None in healthy system (self-serve autonomy)

**Non-preferred alternatives that caused confusion:**

- ❌ "Site Assignment" (implies campground chooses; removes autonomy)
- ❌ "Site Reservation" (implies pre-assignment; frontloads the decision)
- ❌ "Pre-registration site selection" (contradictory; you can't select well pre-arrival)
- ❌ "Reserving a specific site" (pre-arrival, sight-unseen decision)
- ❌ "Site Preference" (too weak; implies optional)

**Why precision matters:** "Selection" vs. "Assignment" is the difference between autonomy and control. The old system was selection (you pick). The new system is assignment (system picks for you). These send very different signals.

---

## Supporting Terminology

### Site-Level Observations

| Term                             | Definition                                | Observable? | When?                                          |
|----------------------------------|-------------------------------------------|-------------|------------------------------------------------|
| **Site Vacancy**                 | Physical site is currently unoccupied     | Yes         | On-site, by visual inspection                  |
| **Site Availability (database)** | Database rules permit selecting this site | No          | Requires app/query; often differs from vacancy |
| **Unoccupied Site**              | No camper currently set up there          | Yes         | On-site, by observation                        |

**Why this distinction matters:** In the old system, vacancy = availability. In the new system, a site can be vacant but unavailable (locked for future bookings, held due to timeout, etc.). This gap is where autonomy gets trapped.

---

### Commitment Types (What Gets Decided and When)

| Commitment                    | Definition                      | When Made                                          | Who Commits       | Reversible?                                           |
|-------------------------------|---------------------------------|----------------------------------------------------|-------------------|-------------------------------------------------------|
| **Campground Commitment**     | CG commits capacity to camper   | Pre-arrival (ASAP)                                 | Campground system | Only if camper cancels                                |
| **Camper Payment Commitment** | Camper commits funds            | Pre-arrival or at arrival                          | Camper            | Yes, but friction increases if pre-arrival            |
| **Camper Site Commitment**    | Camper commits to specific site | On-site, at arrival (or pre-arrival in bad system) | Camper            | Easy if at arrival; requires staff/app if pre-arrival |

**Why this distinction matters:** These three can be decoupled. The new system coupled them all pre-arrival. The better system: Campground Commitment pre-arrival, Site Commitment at arrival.

---

## What Not to Say

### Confusing Pairings

❌ **"Reservation System"** -- too vague; includes both registration and site assignment without distinguishing them  
✅ **"Registration system with capacity commitment"** or **"Pre-arrival registration with on-site site selection"**

❌ **"The system moved site selection online"** -- doesn't distinguish from moving capacity commitment  
✅ **"The system coupled site selection to registration, moving both pre-arrival"**

❌ **"Guaranteeing availability"** -- unclear if capacity-wide or site-specific  
✅ **"Guaranteeing capacity commitment" or "guaranteeing an unoccupied site upon arrival"**

❌ **"Pre-registration"** -- doesn't specify what's happening pre-arrival  
✅ **"Pre-arrival registration (capacity commitment + payment) with site selection deferred to arrival"**

---

## Common Mistakes & How to Avoid Them

### Mistake 1: Conflating Registration and Site Selection

**Bad:** "The old system required registration at arrival."  
**Better:** "The old system deferred registration (capacity commitment + payment) to arrival, along with site selection."  
**Why:** Registration and site selection are separable. Showing they were bundled at arrival explains why decoupling them helps.

### Mistake 2: Using "Reservation" for Everything

**Bad:** "The new reservation system lets people reserve ahead."  
**Better:** "The new system lets people register (commit capacity + payment) ahead. Sites are pre-assigned in the same system."  
**Why:** "Reservation" doesn't clarify what's being reserved (capacity vs. site).

### Mistake 3: Saying "Availability" When You Mean "Vacancy"

**Bad:** "Vacant sites in the database show as available."  
**Better:** "Physically vacant sites may not be available in the database (due to future bookings or system holds)."  
**Why:** This gap is where the coupling problem manifests.

### Mistake 4: Treating "Selection" and "Assignment" as Synonyms

**Bad:** "The system assigns sites to campers."  
**Good:** "The system pre-assigns sites (the system chooses for you)."  
**Better:** "The old system let campers select sites on-site. The new system pre-assigns them before arrival."  
**Why:** The verb choice signals who has autonomy. Precision matters.

---

## Terminology in Context: The Three Stories

### Jan and Her Dog

**What breaks:** Site Selection is pre-assigned (assignment, not selection) before arrival. Upon arrival, she discovers her assigned site has an electric fence. She wants to select a different site (change her selection), but the system requires staff intervention to modify the pre-assignment.

**Terminology:** "Jan had to request staff intervention to change her pre-assigned site to one she could actually select on-site."

### Steven & Friends

**What breaks:** Site Selection is pre-assigned (assignment, not selection) before arrival. Upon arrival, the assigned site is sunnier than expected. He could select (move to) a shady site, but changing the pre-assignment has friction.

**Terminology:** "Steven's assigned site didn't match his preference. Switching sites would require app friction or staff help, so he accepted his assigned site."

### Kevin in a Hammock (Walk-In)

**What breaks:** Kevin wants to select a site on-site, but the system times out while he's trying to register. A provisional hold is placed, locking him into his second choice.

**Terminology:** "Kevin's attempted site selection was interrupted by a system timeout, which created a provisional hold that removed his autonomy to select freely."

---

## Reference: Old vs. New Terminology

| Concept             | Old System              | New System                             | Standard Term                                    |
|---------------------|-------------------------|----------------------------------------|--------------------------------------------------|
| Admission guarantee | Not guaranteed          | Guaranteed pre-arrival                 | Capacity Commitment                              |
| Payment timing      | At arrival              | Pre-arrival                            | Part of Registration                             |
| Site choice         | Self-serve at arrival   | Pre-assigned before arrival            | Site Selection → (unfortunately) Site Assignment |
| Who decides site    | Camper                  | System                                 | Camper (standard) vs. System (current)           |
| Site freedom        | High (pick from vacant) | Low (locked unless changed with staff) | Autonomy level                                   |
| Staff involvement   | Rare (exceptions only)  | Regular (conflicts from mismatches)    | Staff service frequency                          |
