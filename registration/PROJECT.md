# Registration Process -- LinkedIn Article

## Goal

Create a LinkedIn article that is a case study in process-aware system design. Specifically: how automation can invisibly couple separate processes, and why regression testing (checking what broke) is as important as validating what improved.

## Primary Summary

**Decisions are not simply about an ultimate selection result. Aspects of the deciding process affect the quality of the decision, and the satisfaction of the deciders.**

## Professional Positioning

This article showcases expertise in:

- **Process definition and technical analysis** -- understanding what a system actually does, not just what it's intended to do
- **Don't automate bad processes** -- full-featured systems make it easy to move multiple processes together without noticing
- **Analyze from customer perspective with multiple use cases** -- one improved outcome (capacity guarantee) doesn't mean the system improved overall (site selection degraded)
- **Regression testing mindset** -- when you change one thing, ask "what else broke?" Did something go backwards?
- **Signaling matters** -- it's not just about technical outcomes; systems send signals about trust, autonomy, respect

## Secondary Purpose

This article is framed as a professional case study suitable for LinkedIn. It can also serve as a foundation for a proposal to Aaron if/when he is receptive to discussing how the new registration system improves one aspect (capacity guarantee/peace-of-mind) while severely degrading another (site selection autonomy and quality).

Current understanding: Wendy's coaching is that we are not invited to propose changes. But the value is in articulating the tradeoff clearly--so that if Aaron becomes aware of the customer harm, he has a framework for understanding it rather than just complaints.

## Key Themes to Weave

1. **Solving for one thing is not sufficient** -- Jan's peace of mind about guaranteed admission doesn't help if her actual experience is worse (locked into wrong site, needs staff help)
2. **Regression testing for processes** -- Did something regress? Go backwards? In this case: site selection went from self-serve to staff-dependent; conflicts increased despite automation
3. **Multiple use cases, multiple perspectives** -- Offsite pre-regs (Jan, Steven) AND walk-ins (Kevin) AND staff efficiency all affected differently
4. **Signaling is not separate from function** -- Systems that say "we trust you" vs. "you need permission" send different messages. The message matters.

## Raw Material

See [`raw_rambling.md`](./raw_rambling.md) for unedited notes, observations, and framework dimensions.

## Structure (TBD)

Story arcs and reorganization to follow. The raw material is preserved in its original form--stream-of-consciousness, incomplete, with working terminology--to be shaped into polished prose later.

## Chosen Narrative Arc

**Arc 3: "The Invisible Coupling"**

Why this arc:

- Systems and automation focused (aligns with professional positioning)
- Highlights the core insight: it's easy to move multiple processes together without noticing
- Shows how full-featured platforms enable invisible coupling
- Leads naturally to regression testing / "what broke?" analysis
- Allows threading of signaling (not just technical but human experience)

Arc structure:

1. **Hook** -- Easy to build systems that do many things. Hard to notice you're moving multiple processes together.
2. **What Happened** -- Registration needed to move pre-arrival (pace of mind). System had features for registration AND site selection. Both moved.
3. **The Oversight** -- Different timing needs weren't surfaced as explicit design choices.
4. **Evidence** -- Jan, Steven, Kevin stories showing where coupling caused friction.
5. **Insight** -- This is easy to overlook when focused on solving one problem.
6. **Summary** -- Be explicit about which features you use, which timing changes you make. Coupling invisibly is easy. Decoupling later is expensive.

## Key Contrasts

The article will compare two systems across process dimensions:

- **Registration** (Capacity Commitment + Payment) -- can move pre-arrival
- **Site Selection** -- should stay at arrival (needs sensory ground truth)

Each system makes different tradeoffs on **timing**, **information**, **autonomy**, and **what signals are sent**.
