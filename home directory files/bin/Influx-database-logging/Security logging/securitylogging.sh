#!/bin/bash

# Directories and files
DIR_BIN=$(dirname $(readlink -f $0))
cd $DIR_BIN
DIR_NAME="/home/EMLI_TEAM_24/Scripts/Security status"
LOG_FILE="/home/EMLI_TEAM_24/log/securitylogging.log"

# Fetch security metrics
CURRENTLY_BANNED=$("$DIR_NAME/currently_banned.sh")
CURRENTLY_FAILED=$("$DIR_NAME/currently_failed.sh")
TOTAL_BANNED=$("$DIR_NAME/total_banned.sh")
TOTAL_FAILED=$("$DIR_NAME/total_failed.sh")

# Post security metrics to InfluxDB
bash "$DIR_BIN/post_to_database.sh" currently_banned "$CURRENTLY_BANNED" rpi_security
bash "$DIR_BIN/post_to_database.sh" currently_failed "$CURRENTLY_FAILED" rpi_security
bash "$DIR_BIN/post_to_database.sh" total_banned "$TOTAL_BANNED" rpi_security
bash "$DIR_BIN/post_to_database.sh" total_failed "$TOTAL_FAILED" rpi_security

# Log the metrics to a file
{
    echo "Time: $(date '+%A, %d %B %Y %H:%M:%S %Z')"
    echo "Current failed attempts: $CURRENTLY_FAILED"
    echo "Total failed attempts: $TOTAL_FAILED"
    echo "Current bans: $CURRENTLY_BANNED"
    echo "Total bans: $TOTAL_BANNED"
} >> "$LOG_FILE"

# Ensure the log file does not exceed 6000 lines
tail -n 4000 "$LOG_FILE" > temp.log && mv -f temp.log "$LOG_FILE"