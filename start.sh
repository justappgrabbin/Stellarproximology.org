#!/bin/bash
# Substrate Engine Startup Script

echo "[INIT] Substrate Engine"

# Clone Substrate repo if not present
if [ ! -d "Substrate" ]; then
    echo "[CLONE] Getting Substrate repo..."
    git clone --depth 1 https://github.com/danielmiessler/Substrate.git
fi

# Install deps
pip install -r requirements.txt

# Start server
echo "[START] Launching API..."
python main.py
