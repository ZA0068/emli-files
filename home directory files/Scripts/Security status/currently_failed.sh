#!/bin/bash
sudo fail2ban-client status sshd | awk '/Currently failed:/ {print $5}'