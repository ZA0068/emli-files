#!/bin/bash
echo $(free -m | grep Mem | awk '{print ($4/$2)*100}' | sed 's/,/./g')
