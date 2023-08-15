#!/bin/bash
DIR_BIN="$(dirname "$(readlink -f "$0")")"
source "$DIR_BIN/calculate_data_transmission.sh" "eth0_rx.sh"