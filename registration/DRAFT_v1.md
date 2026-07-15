# Decisions Are More Than Outcomes: A Case Study in What Gets Coupled

## The Confirmation Notice

---

**GENERAL ADMISSION CONFIRMATION**

**Confirmation #:** GA-20260715-001  
**Camper:** Jan and Dog  
**Visit Duration:** 3 nights  
**Date of Arrival:** July 15, 2026  
**Payment Received:** $XXX  

**What This Means:**

Your payment guarantees you **General Admission** to Trails End Campground for your chosen dates. This means:

- There will be an unoccupied site available for you when you arrive
- You are free to select any unoccupied site you find most pleasing and compatible with your needs
- No pre-assignment. No app interaction at arrival. No stop at the welcome board required.
- Just show up, drive around, find the site that feels right, and set up.

**No Further Action Needed.** Once you have this confirmation, you're all set. See you soon.

---

## The Three Stories (Updated)

### 1. Jan and Her Dog

**Before Arrival:**

Jan sits at home, books her 3-night stay, and receives the General Admission confirmation above. She reads it: *just show up, select any unoccupied site you find most pleasing.* She feels relief (guaranteed admission) and anticipation (she gets to choose).

**Upon Arrival:**

Jan drives into the campground. She walks around with her dog, observing sites. She notices a couple have electric fences nearby--those are out. She finds a perfect site: open enough for her dog to roam, shaded, quiet, near water. She sets up.

**What Happened:**

- Zero staff interaction (except for her interest to).
- Zero app interaction at arrival.
- Jan got the right site for her needs, based on direct observation.
- She feels trusted and respected.

**In the Old System:** Essentially the same. Jan would have paid cash, received verbal or written assurance of admission, arrived, walked around, found the perfect site, and set up. No difference except method of payment.

**In the Current System (Pre-General Admission):** Jan pre-selects a site online, commits to it sight-unseen, arrives to find an electric fence. She has to find Wi-Fi, launch an app, discover that "vacant" doesn't mean "available" in the database, and track down someone with admin access to change her reservation.

---

### 2. Steven & Friends

**Before Arrival:**

Steven books for his group and receives the General Admission confirmation. He shares it with his friends: *just show up, select any site you find most pleasing.*

**Upon Arrival:**

Steven and friends spend 30 minutes walking the campground together. They discuss what they want. "We'd prefer shade." They find a shady spot with great views. Someone says "this one feels right." They set up.

**What Happened:**

- The site-selection process itself was collaborative and social--part of the trip experience.
- They got the site they actually wanted, not a compromise.
- Zero staff interaction.
- Zero app friction.

**In the Old System:** Same outcome.

**In the Current System (Pre-General Admission):** Steven pre-selects a site, arrives to discover it's sunnier than expected. He could switch, but it requires an app interaction or finding staff. He decides it's not worth the friction, and he sweats it out.

---

### 3. Kevin in a Hammock (Walk-In)

**Upon Arrival:**

Kevin shows up unannounced. He's been here before, back when the system was simpler. He drives to the welcome board, sees the General Admission process posted, understands: *select any unoccupied site.* He drives around, finds a site with a perfect tree for his hammock and a good view, and sets up.

**What Happened:**

- Kevin didn't need to pre-book.
- Zero friction. He saw what was available, chose what he wanted.
- Zero staff interaction.

**In the Old System:** Same. Kevin shows up, asks if there's room, gets yes, selects a site, pays cash, sets up.

**In the Current System (Pre-General Admission):** Kevin tries to book online but the system times out. A provisional hold gets placed. He ends up locked into his #2 choice. Or he decides booking is too much hassle and drives away.

---

## The Key Distinction

Two separate things are being decided:

1. **General Admission** -- Is there room? Can I come? (Campground-level capacity)
2. **Site Selection** -- Which specific site do I occupy? (Individual choice, based on preference and ground truth)

**Old System:** Both happen at arrival, on-site. No guarantee of room beforehand; full information for site selection.

**New System (with General Admission):** General Admission happens offsite and early (peace of mind). Site Selection happens on-site and on-arrival (full sensory information).

**Pre-General Admission System:** Both moved offsite and early. Site selection lost information and autonomy. Conflicts became more common because site assignments were made without ground truth.

---

## Why the Distinction Matters

When you couple General Admission with Site Selection in a single system, two things happen:

1. **You commit to site timing based on admission timing.** To guarantee General Admission early, you feel forced to also assign specific sites early--because the system can do it. But these don't have to be coupled.

2. **You create staff dependencies.** When someone arrives and their pre-assigned site isn't what they wanted (wrong sun, wrong vibe, proximity issue), they need staff to intervene. In the old system, they just moved. Zero staff time.

**The General Admission approach decouples them:** Guarantee capacity early (peace of mind), defer site selection to arrival time (ground truth + autonomy).

---

## Terminology: Getting Precise

We need clear terms for the two different commitments:

| Concept               | Definition                                                                   | Timing              | Information                               | Decision Maker |
|-----------------------|------------------------------------------------------------------------------|---------------------|-------------------------------------------|----------------|
| **General Admission** | Campground guarantees an unoccupied site will be available upon your arrival | Offsite, ASAP       | Current capacity + business rules         | Campground     |
| **Site Selection**    | Individual camper chooses which specific site to occupy                      | On-site, at arrival | Sensory observation + personal preference | Camper         |

**Why this matters:** You can offer one without the other. General Admission alone doesn't require pre-assigning sites. Site Selection alone doesn't require an advance guarantee. They're logically independent. But once you build a system that can do both, it's easy to move both to the same timing, invisibly coupling them.

---

## The Professional Insight

**The Problem:** In trying to solve one legitimate issue (no General Admission guarantees scaring off guests), a full-featured online system was deployed that also moved Site Selection offsite. Both used the same technical infrastructure. No one explicitly said "let's couple these"--it just happened because the system had the features.

**The Oversight:** The distinction between "guaranteeing capacity" and "assigning specific sites" didn't surface as an explicit design choice. When you're focused on solving the admission problem, it's easy not to notice you've changed the site selection process.

**The Consequence:** General Admission improved. But Site Selection degraded because it lost sensory information and autonomy. More conflicts arose because site assignments were made without ground truth. Staff time increased (the opposite of what you'd expect from automation).

**The Lesson:** When you're changing one aspect of a system, be explicit about what else you're changing. Full-featured platforms make it easy to move multiple decisions together--but that doesn't mean you should. Sometimes the best system decouples decisions, letting each one happen at the right time with the right information.

---

## The Owner's Vision

The owner built a campground with extraordinary variety: morning sun, evening sun, all-day sun, open feel, cozy feel, lake views, mountain views, orchard views, sites for groups, sites for solitude, easy pull-throughs, castle-hill tent sites.

That richness is intentional. The original system--walk around, observe, choose--honored that richness. Site selection was an experience: you and your companions wandered, discussed, felt the vibe, and picked the site that felt right.

The new system tried to add peace of mind (General Admission) and accidentally removed autonomy and joy from site selection.

The General Admission approach keeps both. It says: "We guarantee you'll have a site. And when you get here, you get to experience the richness of choosing."

---

**NEXT: Refine terminology, review story arcs, adjust framing.**
