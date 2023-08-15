#!/bin/bash
sudo fail2ban-client status sshd | awk 'BEGIN {ORS=" "} /Banned IP list:/ {for (i=5; i<=NF; i++) print $i}'