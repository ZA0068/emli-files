# emli-files

This will mostly work on Raspberry Pi 4 with ubuntu server installed.
If you already have one then copy all:

* files and folders in the *home directory files* folder into
´´´sh
 /home/*USER*/
´´´


* files and folders in the *etc directory files* folder into
´´´sh
/etc/
´´´

* files and folders in the *var directory files* folder into
´´´sh
/var/
´´´

for the latter two, remember to run ´´´sh sudo systemctl daemon-reload´´´ and run 
´´´sh
sudo systemctl enable *services*
sudo systemctl start *services*
sudo systemctl enable *timers*
sudo systemctl start *timers*
