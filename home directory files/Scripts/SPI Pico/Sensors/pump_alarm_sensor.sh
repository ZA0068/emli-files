#!/bin/bash
exec 3<>/dev/ttyACM0
read -r line <&3  #/tmp/read_device_pipe

element=$(echo "$line" | cut -d ',' -f 2 | tr -d '[]')
echo "$element"

#exec 3<&-
#exec 3>&-
