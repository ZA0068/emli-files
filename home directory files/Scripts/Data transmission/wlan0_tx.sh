#!/bin/bash
DIR_BIN="$(dirname "$(readlink -f "$0")")"
source "$DIR_BIN/get_data_transfer.sh" wlan0 10