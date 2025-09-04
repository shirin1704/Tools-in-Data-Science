#!/usr/bin/env bash
# Usage: ./make_pr.sh <your-github-repo-ssh-or-https-url>
set -euo pipefail

REPO_URL="${1:-}"
if [ -z "$REPO_URL" ]; then
  echo "Provide your GitHub repo URL, e.g.:"
  echo "  ./make_pr.sh git@github.com:your-org/mrr-analysis.git"
  exit 1
fi

WORKDIR="$(pwd)"
BRANCH="feat/mrr-2024-analysis"

git init
git checkout -b "$BRANCH"
git add .
git commit -m "Add 2024 MRR analysis, visuals, and data story (author: 23f2003577@ds.study.iitm.ac.in)"
git remote add origin "$REPO_URL"
git push -u origin "$BRANCH"

if command -v gh >/dev/null 2>&1; then
  gh pr create --fill --title "2024 MRR Growth: Analysis & Data Story" --body "Includes analysis code, visualizations, and README with actionable recommendations."
else
  echo "Now open a PR on GitHub from branch $BRANCH."
fi
