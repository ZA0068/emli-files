#!/bin/bash

exec 3<>/dev/ttyACM0

 read -r line<&3
 #while true; do
 element=$(echo "$line" | cut -d ',' -f 1|tr -d '[]')

 echo "$element"
#break
#done
#exec 3<&-
#exec 3>&-
