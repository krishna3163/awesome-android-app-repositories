# Android Repo Radar

Automatically curated collection of open-source apps, tools, websites and repositories discovered from selected Telegram channels.

<!-- AUTO-GENERATED-START -->
## 📊 Statistics

- **Total Projects:** 0
- **Categories:** 0
- **Last Updated:** —

---

## 📋 All Projects

| Project | Description | Repository | Tags |
|:---|:---|:---|:---|
| _No projects yet._ | — | — | — |

<!-- AUTO-GENERATED-END -->

---

## 🚀 Setup & Local Development

### Prerequisites
- Python 3.12+
- Telegram API credentials (from [my.telegram.org](https://my.telegram.org))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/krishna3163/awesome-android-app-repositories.git
   cd awesome-android-app-repositories
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Generate Telegram session string:**
   ```bash
   python scripts/generate_session.py
   ```
   Follow the prompts to enter your API ID, API Hash, phone number, and 2FA code. This will output a `TELEGRAM_SESSION_STRING`.

5. **Configure environment:**
   ```bash
   cp .env.example .env
   ```
   Fill in `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, and `TELEGRAM_SESSION_STRING` in your `.env`.

6. **Run synchronization:**
   ```bash
   # Dry-run mode (check without saving changes):
   python -m src.main --dry-run

   # Full sync:
   python -m src.main
   ```

---

## ⚙️ GitHub Actions & Automation

The repository is synchronized automatically on a schedule via GitHub Actions:
- **Hourly sync:** Runs `0 * * * *` to fetch and sync newly published apps.
- **Manual trigger:** Use `workflow_dispatch` in GitHub Actions UI with optional `dry_run` or `force_resync` flags.

### Required GitHub Secrets

Configure the following secrets in **Settings > Secrets and variables > Actions**:

| Secret | Description |
|---|---|
| `TELEGRAM_API_ID` | Your Telegram API ID from [my.telegram.org](https://my.telegram.org) |
| `TELEGRAM_API_HASH` | Your Telegram API Hash from [my.telegram.org](https://my.telegram.org) |
| `TELEGRAM_SESSION_STRING` | Generated session string from `scripts/generate_session.py` |

---

## 🧪 Running Tests

```bash
# Run test suite
pytest

# Run tests with coverage
pytest --cov=src
```

---

## 📂 Repository Structure

```text
├── .github/workflows/
│   ├── sync.yml              # Scheduled & dispatch Telegram sync workflow
│   └── validate.yml          # Pull request & push validation
├── assets/apps/              # Downloaded cover images and screenshots
├── data/
│   ├── apps.json             # Main project database (Single Source of Truth)
│   ├── pending-features.json # Features awaiting matching project
│   ├── review-required.json  # Low-confidence fuzzy matches for review
│   ├── failed-posts.json     # Malformed posts logs
│   └── processed-messages.json # Message ID offset tracker
├── scripts/
│   └── generate_session.py   # One-time Telegram session generator
├── src/
│   ├── database/             # JSON repository & smart merger
│   ├── generators/           # Marker-based README generator
│   ├── matching/             # Normalization, RapidFuzz & multi-step matching
│   ├── parsers/              # Main channel & features channel parsers
│   ├── telegram/             # Telethon client, monitor & media downloader
│   └── utils/                # Hashing, logging & validators
└── tests/                    # Comprehensive unit and integration test suite
```

---

## 📄 License

This repository is maintained for informational and archival purposes. All projects cataloged belong to their respective authors and licenses.