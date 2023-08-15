#!/bin/bash

exec 3<>/dev/ttyACM0

#echo "1"
read -r line<&3

#echo "2"

 element=$(echo "$line" | cut -d ',' -f 4 | tr -d '[]')

 echo "$element"

#exec 3<&-
#exec 3>&-
