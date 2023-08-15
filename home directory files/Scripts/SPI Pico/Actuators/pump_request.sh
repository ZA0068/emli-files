#!/bin/bash
#yo
#rshell -p /dev/ttyACM0 repl pyboard 'exec(open(\"./water_pump_control.py\").read())'~


exec 3<>/dev/ttyACM0 


echo "p" >&3

exec 3<&-
exec 3>&-
