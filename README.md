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

## 🧪 Python CI + Simulated CD Workflow

This project uses GitHub Actions to automatically test and simulate deployment on every push to the `main` branch.

### 📂 Workflow File
The workflow is defined in:


### 🚀 Trigger

The workflow runs on:
- Pushes to the `main` branch
- Changes to any `*.py` file, `requirements.txt`, or the workflow file itself

### 🔍 What It Does

#### ✅ Test Job
- Runs on Ubuntu
- Executes tests against Python versions: **3.8**, **3.10**, and **3.12**
- Installs dependencies from `requirements.txt`
- Runs tests using `pytest`

#### 🚀 Deploy Job (Simulated)
- Runs only after all tests pass
- Echoes a deployment message into `deployment.log`
- Uploads the log as a GitHub Actions artifact

### 📦 Artifacts
After successful simulated deployment, a file named `deployment.log` is uploaded and can be downloaded from the workflow run page.

---




