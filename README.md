# github-actions-practice
# GitHub Actions CI/CD Test Repo

This repository is for learning and testing GitHub Actions with simple CI/CD workflows.

## Workflows

### 1. Hello World CI
- Trigger: `workflow_dispatch`
- Action: Prints "Hello from GitHub Actions!"

### 2. Tree Listing
- Trigger: `workflow_dispatch`
- Action: Lists repo files in a tree format.

### 3. Simulated CD
- Trigger: On push to `hello.py`
- Action:
  - Runs `hello.py`
  - On success: moves it to `deployed/`
  - Auto-commits the move using GitHub Actions bot

## Branch Strategy

- `main`: Production branch
- `feature-*`: Used for changes and testing

---

## How to Trigger Workflows

- Go to `Actions` tab → choose a workflow → Click **"Run workflow"** if `workflow_dispatch`.

---

## Notes

- Secrets used: `${{ secrets.GITHUB_TOKEN }}`
- GitHub bot used for committing moved files

- ### ✅ GitHub Actions CI Workflow - Update Log

**📅 Date:** June 2, 2025  
**🔧 Changes Implemented:**
- Created a `pytest`-based CI workflow using GitHub Actions
- Debugged a syntax error in the `runs-on: ubuntu-latest` line (was misspelled)
- Successfully executed the workflow after fixing the syntax error
- Added a new function `subtract()` in `main.py`
- Updated `test_main.py` with corresponding test cases for `subtract()`
- Confirmed that the workflow triggers and passes on code push

**🧠 Key Learnings:**
- GitHub Actions runs on any push to `main` unless paths are explicitly defined
- `pytest` automatically discovers and runs files named like `test_*.py`
- CI pipeline now validates functional changes through automated testing

**📌 Next Steps Planned:**
- Implement matrix strategy to test across Python versions
- Add a simulated CD step (e.g., log file output after test success)
- Try EC2 self-hosted runner setup later this week
- Continue exploring DevOps tools and GitHub Actions patterns

