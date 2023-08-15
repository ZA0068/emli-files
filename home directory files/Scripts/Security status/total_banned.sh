#!/bin/bash
sudo fail2ban-client status sshd | awk '/Total banned:/ {print $4}'