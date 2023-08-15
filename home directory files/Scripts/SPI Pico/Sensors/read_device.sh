#!/bin/bash

# Continuously check for device and read from it when present
#while true; do

    # Check if the device is present
 #   if [ -r /dev/ttyACM0 ]; then
        # Open /dev/ttyACM0 for reading
  #      exec 3< /dev/ttyACM0

        # Continuously read data from the device
   #     while read -r line <&3; do
    #       [[ -z "$line" ]] && continue
     #       echo "$line" > /tmp/read_device_pipe
      #  done


        # Close the file descriptor
       # exec 3<&-
   # else
      #  echo "Device not found. Waiting for device to connect..."
      #  sleep 10
   # fi
#done
