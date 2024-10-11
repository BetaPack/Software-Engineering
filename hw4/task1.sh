#!/bin/bash
# Find the process ID (PID) of infinite.sh and kill it

# Get the PID of the running infinite.sh script
pid=$(pgrep -f infinite.sh)

# Check if the process is running
if [ -z "$pid" ]; then
    echo "infinite.sh is not running."
else
    # Kill the process
    kill $pid
    echo "Killed infinite.sh process with PID: $pid"
fi

