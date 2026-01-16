# children-repo-example
A children repository which will push code to the central repo

## GitHub Actions Workflow

This repository includes a GitHub Actions workflow that automatically pushes the contents of the `dags/` folder to the central repository (`nicor88/central-repo-example`).

### Setup

To enable the workflow, you need to configure the following secret in your GitHub repository settings:

1. **CENTRAL_REPO_TOKEN**: A Personal Access Token (PAT) or GitHub App token with write access to the central repository (`nicor88/central-repo-example`)

### How to create a Personal Access Token:

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with `repo` scope
3. Add it as a secret named `CENTRAL_REPO_TOKEN` in this repository's settings

### Workflow Behavior

The workflow triggers when:
- Changes are pushed to `main` branch that affect files in the `dags/` folder
- Manually triggered via workflow_dispatch

The workflow will:
1. Checkout this repository
2. Checkout the central repository (`nicor88/central-repo-example`)
3. Copy all contents from `dags/` to `central-repo-example/children-repo-example/`
4. Commit and push the changes to the central repository
