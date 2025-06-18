#!/bin/bash

# Navigate to the script's directory (important if you run it from elsewhere)
SCRIPT_DIR=$(dirname "$0")
cd "$SCRIPT_DIR"

# Activate the virtual environment
source venv/bin/activate

# Run the Python script
python main.py

