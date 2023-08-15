#!/bin/bash
cat /sys/class/thermal/thermal_zone0/temp | column -s $'\t' -t | sed 's/\(.\)..$/.\1/'