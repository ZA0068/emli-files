#!/bin/bash
sudo fail2ban-client status sshd | awk '/Currently banned:/ {print $4}'