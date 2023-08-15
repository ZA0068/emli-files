#!/bin/bash

# Main function to calculate data transfer rate
calculate_rate() {
    local -i initial=$1
    local -i final=$2
    local -i diff_bytes=$((final - initial))
    echo "${diff_bytes}"
}

# Invoke main function with script arguments
calculate_rate $1 $2