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
