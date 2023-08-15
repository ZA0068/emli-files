#!/bin/bash
source /opt/ros/humble/setup.bash
source /home/EMLI_TEAM_24/ros2ws/install/setup.bash
cd /home/EMLI_TEAM_24/ros2ws/
ros2 launch pumpcontroller pumpcontroller_launcher.py&
ros2 launch plotlogger plotlogger_launcher.py&
wait