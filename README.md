# Himnadi
Pronounced _him-nadi_ aka Glacier in Nepali.

Building a satellite tracking system for climate change. 

Open-source tooling to monitor Himalayan glacial lakes and glacier instability, and to give early warning of Glacial Lake Outburst Floods (GLOFs) and glacier/rock-avalanche-triggered floods in Nepal. The goal is to generate text message to make general public aware of any danger, even few minutes, can save lives.

## Why this exists

On August 26, 2026, a section of glacier and bedrock collapsed above the Lhende River near the Nepal-Tibet border (close to Langtang Lirung). The collapse likely dammed the river, forming a temporary lake that burst and sent a wall of water, ice, mud, and debris more than 60 miles downstream through Rasuwa and Nuwakot districts, killing hundreds of people with over a thousand still missing. There was little to no warning.

This is not an isolated event. The Hindu Kush Himalaya is undergoing rapid glacier loss and permafrost degradation, which increases the risk of cascading hazards: glacier/rock avalanches, glacial lake formation and outburst, and downstream flash flooding. Nepal has thousands of glacial lakes, dozens of which are already classified as potentially dangerous, and most valleys downstream have no real-time monitoring or automated alerting.

## Goal

Build a pipeline that:
1. **Detects** glacial lake changes and glacier instability using free satellite imagery (Sentinel-1/2, Planet, Landsat) and DEM data.
2. **Flags** rapid changes (new lake formation, rapid lake growth, visible crevassing/serac instability, moraine dam weakening) against historical baselines.
3. **Alerts** relevant people (researchers, local authorities, downstream communities) faster than manual satellite review currently allows, if there is any. The goal is to generate text message to make general public aware of any danger so we can save lives.
4. Stays **open and reproducible** so glaciologists, Nepali government agencies (ICIMOD, DHM), and local communities can inspect, extend, or fork it.

This is not a replacement for in-situ sensors or professional hazard assessment, it's meant to lower the barrier to continuous, automated screening, which today largely doesn't exist for most of these valleys.

## Project status

Early scaffold. Nothing here is production-ready or validated against real hazard data yet. See [docs/roadmap.md](docs/roadmap.md).

## Repo layout

```
glacier-watch-nepal/
├── src/
│   ├── data_sources.py        # satellite/DEM data fetch clients (Sentinel Hub, Planet, etc.)
│   ├── lake_detection.py      # water-body / glacial lake extraction from imagery
│   ├── change_detection.py    # time-series comparison, anomaly flagging
│   ├── alerting.py            # notification hooks (email, SMS, webhook)
│   └── config.py              # region-of-interest + threshold config
├── data/                      # local cache / sample data (gitignored except samples)
├── docs/
│   └── roadmap.md
├── tests/
├── .github/workflows/         # CI (lint/test on push)
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Getting started

```bash
git clone https://github.com/<your-username>/glacier-watch-nepal.git
cd glacier-watch-nepal
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

See `src/config.py` for how to define a region of interest (a glacial lake or glacier front) to monitor.

## Data sources to evaluate

- **Sentinel-1** (SAR, works through cloud cover, critical in the monsoon-shadowed Himalaya) and **Sentinel-2** (optical, 10m) via Copernicus / Sentinel Hub, free.
- **Planet Labs** — higher resolution, was used by researchers to reconstruct the Aug 26 collapse; commercial but has research/disaster-response access programs.
- **ICIMOD** glacial lake inventories (Hindu Kush Himalaya region) — existing baseline datasets to build on rather than starting from zero.
- **ASTER / ArcticDEM / Copernicus DEM** — for terrain and elevation-change analysis.
- **USGS** seismic data — the Aug 26 collapse registered as a magnitude ~5.2 event on local seismometers, which is a possible secondary detection signal.

## Contributing

This is meant to be a community effort, not a solo project. If you have glaciology, remote sensing, hazard modeling, or Nepal-based disaster response experience, please open an issue, even just to point out what's naive about the current approach.

## Questions / feedback

Have a question, suggestion, or want to help? [Email longshahllc@gmail.com](mailto:longshahllc@gmail.com)
## License

MIT — see [LICENSE](LICENSE).

