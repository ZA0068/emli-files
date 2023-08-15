#!/bin/bash

# Directories and temporary files
DIR_BIN=$(dirname $(readlink -f $0))
DIR_NAME="/home/EMLI_TEAM_24/Scripts"
LOG_FILE="/home/EMLI_TEAM_24/log/networklogging.log"

TEMP_ETH0_RECV="/tmp/eth0_recv.tmp"
TEMP_ETH0_TRANS="/tmp/eth0_trans.tmp"
TEMP_WLAN0_RECV="/tmp/wlan0_recv.tmp"
TEMP_WLAN0_TRANS="/tmp/wlan0_trans.tmp"
TEMP_INTERNET_CONNECTION="/tmp/internet_connection.tmp"

# Fetch network metrics
ETH0_RECV=$("$DIR_NAME/Data transmission/eth0_data_received.sh")
ETH0_TRANS=$("$DIR_NAME/Data transmission/eth0_data_transmitted.sh")
WLAN0_RECV=$("$DIR_NAME/Data transmission/wlan0_data_received.sh")
WLAN0_TRANS=$("$DIR_NAME/Data transmission/wlan0_data_transmitted.sh")
INTERNET_CONNECTION=$("$DIR_NAME/Network status/check_internet.sh")

# Post metrics to InfluxDB
bash "$DIR_BIN/post_to_database.sh" eth0_data_received "$ETH0_RECV" rpi_network
bash "$DIR_BIN/post_to_database.sh" eth0_data_transmitted "$ETH0_TRANS" rpi_network
bash "$DIR_BIN/post_to_database.sh" wlan0_data_received "$WLAN0_RECV" rpi_network
bash "$DIR_BIN/post_to_database.sh" wlan0_data_transmitted "$WLAN0_TRANS" rpi_network
bash "$DIR_BIN/post_to_database.sh" internet_connection_status "$INTERNET_CONNECTION" rpi_network

# Log the metrics to a file
{
    echo "Time: $(date '+%A, %d %B %Y %H:%M:%S %Z')"
    echo "eth0 data received: $ETH0_RECV"
    echo "eth0 data transmitted: $ETH0_TRANS"
    echo "wlan0 data received: $WLAN0_RECV"
    echo "wlan0 data transmitted: $WLAN0_TRANS"
    echo "Is internet connected: $INTERNET_CONNECTION"
} >> "$LOG_FILE"

# Ensure the log file does not exceed 6000 lines
tail -n 6000 "$LOG_FILE" > temp.log && mv -f temp.log "$LOG_FILE"