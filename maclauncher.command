#!/bin/bash
# macOS launcher for main.py
cd "$(dirname "$0")"
python3 main.py
read -n 1 -s -r -p "Press any key to exit"

