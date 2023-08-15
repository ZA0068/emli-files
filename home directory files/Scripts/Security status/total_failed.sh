#!/bin/bash
sudo fail2ban-client status sshd | awk '/Total failed:/ {print $5}'