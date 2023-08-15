#!/bin/bash
DIR_BIN="$(dirname "$(readlink -f "$0")")"
initial=$(source "$DIR_BIN/$1")
sleep 1
final=$(source "$DIR_BIN/$1")
source "$DIR_BIN/calculate_diff.sh" "$initial" "$final"