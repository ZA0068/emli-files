#!/bin/bash
ping -c 1 -W 1 8.8.8.8 &> /dev/null && echo 1 || echo 0
