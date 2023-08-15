#!/bin/bash
interface=$1
column=$2
cat /proc/net/dev | grep "$interface" | awk -v col=$column '{print $col}' | tr -d '\n'