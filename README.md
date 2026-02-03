# UC.Zone API v2 Documentation - Umbrella Dota 2

Documentation for developing Lua 5.4 scripts for the Umbrella Dota 2 cheat using UC.Zone API v2. This repository contains the automatically updated documentation and the tools used to generate it.

## 📋 General Information

- **API Version**: UC.Zone API v2
- **Programming Language**: Lua 5.4
- **Last Update**: 02.02.2026
- **Official Website**: [uc.zone/ru/dota2](https://uc.zone/ru/dota2)

## 📁 Repository Structure

This repository contains the following key files and directories:

- **`DocumentationUCZONE.md`**: The main generated documentation file containing all API references, functions, and classes.
- **`main.py`**: The Python script responsible for parsing the source documentation and generating the Markdown file.
- **`requirements.txt`**: List of Python dependencies required to run the parser script.
- **`urls.txt`**: A text file containing the URLs used by the parser to fetch documentation data.
- **`lua-5.4-manual.pdf`**: The official Lua 5.4 reference manual included for offline developer reference.
- **`.github/workflows/`**: Directory containing CI/CD configurations for automated updates.

## 🤖 Workflows & Automation

This project utilizes GitHub Actions to ensure the documentation remains current.

### 1. Update Documentation (`update-documentation.yml`)
- **Schedule**: Runs automatically every day at **20:00 MSK (17:00 UTC)**.
- **Trigger**: Can also be triggered manually via `workflow_dispatch`.
- **Process**:
  1. Sets up a Python environment (3.11).
  2. Installs dependencies from `requirements.txt`.
  3. Executes `main.py` to scrape and regenerate the documentation.
  4. Checks for changes in `DocumentationUCZONE.md`.
  5. If changes are detected, commits and pushes the update with a timestamp.

### 2. Update Documentation Date (`update_docs_date.yml`)
- **Trigger**: Runs on push events to `main` (specifically when `DocumentationUCZONE.md` is modified) or on a schedule.
- **Process**:
  1. Retrieves the date of the latest commit.
  2. Automatically updates the "**Last Update**" date string in this `README.md` and `DocumentationUCZONE.md`.
  3. Commits the changes back to the repository.

## 🔧 Local Usage Requirements

To run the documentation parser locally on your machine:

1. **Python 3.11+** is required.
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the parser script:
   ```bash
   python main.py
   ```

## 📞 Support

- **Official Website**: [uc.zone](https://uc.zone/ru/dota2)
- **Updates**: Star and watch this repository to get notified about API updates.

---

**Last Update**: 02.02.2026  
**Author**: Nerve11
