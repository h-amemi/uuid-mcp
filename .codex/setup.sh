#!/usr/bin/env bash
set -euo pipefail

# Install Rye if it's not already available
if ! command -v rye >/dev/null 2>&1; then
  curl -sSf https://rye.astral.sh/get | bash
  source "$HOME/.rye/env"
fi

# Install project and dev dependencies
rye sync
