# Steam Scanner Pro

Professional Steam Market Analyzer built with Python.

Steam Scanner Pro analyzes Steam Market items, calculates an opportunity score based on historical data and exports professional reports.

---

## Features

- Rich terminal dashboard
- Historical price analysis
- Opportunity scoring
- CSV report export
- Modular architecture
- Domain-driven models

---

## Project Structure

```text
app/
├── analysis/
├── database/
├── domain/
├── providers/
├── reports/
├── scanner/
└── ui/
```

---

## Architecture

```text
ScannerService
        │
        ▼
 ScannerEngine
        │
        ▼
 PriceRepository
        │
        ▼
 Analyzer
   ├── Statistics
   ├── Scorer
   └── Recommendation
        │
        ▼
 Dashboard
        │
        ▼
 CSV Exporter
```

---

## Installation

```bash
git clone https://github.com/Khadiz-ctrl/Projetc-Steam-Market

cd Projetc-Steam-Market

python -m venv .venv

pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

---

## Current Status

Version: **0.3.0**

Current Provider:

- Mock Provider

Roadmap:

- Steam Provider
- Alerts
- Historical Analysis
- Discord Integration

---

## License

MIT