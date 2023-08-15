#!/bin/bash
echo $((100 - $(sudo df | grep "/dev/mmcblk0p2" | awk '{print $5}' | tr -d '%')))