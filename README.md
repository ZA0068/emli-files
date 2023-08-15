# EMLI Project source code
## Setup

This will primarily work on Raspberry Pi 4 with the Ubuntu server installed.
If you already have one then copy all:

* files and folders in the *home directory files* folder into
```sh
 cp -r "home directory files"/* /home/$USER/
```

(down there you have to restart services if they are already active or start and enable them if not)

* files and folders in the *etc directory files* folder into
```sh
sudo cp -r "etc directory files"/* /etc/
```

* files and folders in the *var directory files* folder into
```sh
sudo cp -r "var directory files"/* /var/
```

for the latter two, remember to run `sh sudo systemctl daemon-reload` and run 
```sh
sudo systemctl daemon-reload
sudo systemctl enable <service_name>
sudo systemctl start <service_name>
sudo systemctl enable <timer_name>
sudo systemctl start <timer_name>
```

example: 
```bash
sudo systemctl start hostapd
sudo systemctl enable hostapd
```

