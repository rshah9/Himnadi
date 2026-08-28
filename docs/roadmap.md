# Roadmap

## Phase 0 — Foundations (now)
- [ ] Pull existing ICIMOD / Hindu Kush Himalaya glacial lake inventory as a baseline dataset
- [ ] Pick 2-3 known high-risk lakes (e.g. in Rasuwa, Solukhumbu) as first monitoring targets
- [ ] Get Sentinel Hub API access (free tier) and pull a first time series of imagery for one lake
- [ ] Write a basic water-extent extraction script (NDWI thresholding is a reasonable first pass)

## Phase 1 — Change detection
- [ ] Build a time-series store of lake extent / area per site
- [ ] Detect rapid area growth or new lake formation vs. historical baseline
- [ ] Add DEM-based terrain context (slope, upstream glacier extent) per site
- [ ] Backtest against known past GLOF events (e.g. compare imagery in the weeks before known outburst events) to sanity-check the detection logic

## Phase 2 — Alerting
- [ ] Define alert thresholds and severity levels
- [ ] Build a simple notification pipeline (email/webhook first, SMS later — SMS matters most for last-mile reach but is harder logistically)
- [ ] Publish a public dashboard (even a static one) showing monitored sites and current status

## Phase 3 — Validation and partnerships
- [ ] Reach out to ICIMOD, Nepal's Department of Hydrology and Meteorology (DHM), and glaciology researchers to validate the approach and avoid duplicating existing systems
- [ ] Understand what early warning infrastructure already exists (Nepal has some GLOF monitoring efforts) and figure out where this tool adds value rather than overlapping
- [ ] If viable, pilot with a specific downstream community or local authority

## Open questions
- What's the realistic latency from "satellite image captured" to "alert sent," and is that fast enough to matter for fast-onset events like the Aug 26 collapse (which may have had almost no useful lead time regardless)?
- Should this focus on slow-building GLOF risk (weeks-to-months lead time, where satellite monitoring is well-suited) rather than sudden rock/ice avalanches (which may need seismic or acoustic sensors instead)?
- Who is the actual end user — a research institution, DHM, or local communities directly? This affects UX and alerting design a lot.
