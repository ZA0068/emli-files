#!/bin/bash

DIR_BIN=$(dirname $(readlink -f $0))
cd "$DIR_BIN"

# Expanding the ~ to the full path for the home directory
LOG_FILE="/home/EMLI_TEAM_24/log/motorcontrol12h.log"

# Check if the file exists, if not create and add "0"
if [ ! -f "$LOG_FILE" ]; then
    echo "0" > "$LOG_FILE"
else
    # Read the last line (the number), increment it by 1 and append to the file
    LAST_NUM=$(tail -n 1 "$LOG_FILE")
    echo "$((LAST_NUM + 1))" >> "$LOG_FILE"
fi

tail -n 10 "$LOG_FILE" > temp.log && mv temp.log "$LOG_FILE"