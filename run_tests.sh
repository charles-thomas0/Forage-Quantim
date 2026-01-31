#!/usr/bin/env bash

# Exit immediately if any command fails
set -e

# Activate virtual environment
source venv/bin/activate

# Run Dash test suite (headless Firefox)
PYTHONPATH=. pytest --webdriver Firefox --headless

# If pytest succeeds, exit 0 (implicit)
exit 0
