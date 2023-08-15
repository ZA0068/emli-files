#!/bin/bash

# Define directories and files
DIR_BIN=$(dirname $(readlink -f $0))
DIR_NAME="/home/EMLI_TEAM_24/Scripts"
LOG_FILE="/home/EMLI_TEAM_24/log/healthlogging.log"

# Fetch system health metrics
CPU_TEMP=$("$DIR_NAME/CPU status/cpu_temperature.sh")
CPU_USAGE=$("$DIR_NAME/CPU status/cpu_load.sh")
DISK_SPACE=$("$DIR_NAME/Memory status/remaining_disk_space.sh")
RAM=$("$DIR_NAME/Memory status/remaining_ram.sh")

# Post metrics to InfluxDB without units
bash "$DIR_BIN/post_to_database.sh" cpu_temperature "$CPU_TEMP" rpi_health
bash "$DIR_BIN/post_to_database.sh" cpu_usage "$CPU_USAGE" rpi_health
bash "$DIR_BIN/post_to_database.sh" disk_space "$DISK_SPACE" rpi_health
bash "$DIR_BIN/post_to_database.sh" ram "$RAM" rpi_health

# Append units for logging
CPU_TEMP_LOG="${CPU_TEMP} °C"
CPU_USAGE_LOG="${CPU_USAGE}%"
DISK_SPACE_LOG="${DISK_SPACE}%"
RAM_LOG="${RAM}%"
# Log the metrics with units to a file
{
    echo "Time: $(date '+%A, %d %B %Y %H:%M:%S %Z')"
    echo "CPU temperature: $CPU_TEMP_LOG"
    echo "CPU usage: $CPU_USAGE_LOG"
    echo "Remaining disk space: $DISK_SPACE_LOG"
    echo "Remaining RAM: $RAM_LOG"
} >> "$LOG_FILE"

# Ensure the log file does not exceed 5000 lines
tail -n 5000 "$LOG_FILE" > temp.log && mv -f temp.log "$LOG_FILE"