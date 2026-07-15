---
name: repo
description: Triggers when the user runs /repo <repository_name> to create a new GitHub repository under the hemil0102 account.
---

# Create GitHub Repository Skill

This skill allows the agent to automatically initialize, commit, and create a GitHub repository for the user's workspace using `gh` CLI.

## How to execute

When the user enters `/repo <repository_name>`, follow these instructions:

1. **Verify `gh` Path and Login**:
   - Always use `/opt/homebrew/bin/gh` to execute `gh` commands since Homebrew paths might not be in the non-interactive PATH.
   - Run `/opt/homebrew/bin/gh auth status` to verify that the user is logged into the `hemil0102` account.

2. **Initialize Git Repository (if not already initialized)**:
   - Check if a `.git` folder exists. If not, run `git init` and create a standard `.gitignore` (ignoring `.DS_Store`, etc.).
   - Stage all existing files: `git add .`
   - Make an initial commit: `git commit -m "Initial commit"`

3. **Create the GitHub Repository**:
   - Run: `/opt/homebrew/bin/gh repo create <repository_name> --private --source=. --remote=origin --push`
   - If the repository name contains spaces or special characters, sanitize it or wrap it appropriately.

4. **Confirm to the User**:
   - Output the repository URL: `https://github.com/hemil0102/<repository_name>`
