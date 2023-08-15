#!/bin/bash
exec 3<>/dev/ttyACM0

read -r line<&3
element=$(echo "$line" | cut -d ',' -f 3 | tr -d '[]')
echo "$element"

#exec 3>&-
#exec 3<&-
