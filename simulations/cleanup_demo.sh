#!/bin/bash

# Cleanup script to reset the SOC Demo environment
# This clears the mock log files so you can start a fresh simulation.

LOG_DIR="simulations"
LINUX_LOG="$LOG_DIR/mock_auth.log"
WINDOWS_LOG="$LOG_DIR/mock_windows_security.log"

echo "[*] Cleaning up SOC Demo logs..."

if [ -f "$LINUX_LOG" ]; then
    echo "" > "$LINUX_LOG"
    echo "[+] Cleared $LINUX_LOG"
fi

if [ -f "$WINDOWS_LOG" ]; then
    echo "" > "$WINDOWS_LOG"
    echo "[+] Cleared $WINDOWS_LOG"
fi

echo "[!] Demo environment reset. You can now run 'python3 simulations/log_generator.py' for a clean run."
