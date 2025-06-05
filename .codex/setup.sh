#!/usr/bin/env bash
set -euo pipefail

# Install Rye if it's not already available
if ! command -v rye >/dev/null 2>&1; then
  curl -sSf https://rye-up.com/get | bash
  source "$HOME/.rye/env"
fi

# Install project dependencies
rye sync

# Install test dependencies
rye run pip install pytest pytest-asyncio
