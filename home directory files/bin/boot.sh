#!/bin/bash
DIR_BIN=`dirname $(readlink -f $0)`
cd $DIR_BIN

source /opt/ros/humble/setup.bash
source /home/EMLI_TEAM_24/ros2ws/install/setup.bash
bash forward.sh
bash rosrun.sh