#!/bin/bash
# macOS launcher for main.py with larger terminal

# Resize terminal: 40 rows x 120 columns
printf '\e[8;40;120t'

# Change directory to the script's folder
cd "$(dirname "$0")"

# Run the Python script
python3 main.py

# Wait for user input before closing the terminal
read -n 1 -s -r -p "Press any key to exit"
