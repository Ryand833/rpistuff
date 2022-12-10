#!/bin/bash

GREEN='\033[1;32m'
CYAN='\033[0;96m'
RED='\033[0;31m'
NC='\033[0m' #no color


# Fetch python script
# Fetch systemd script
# Daemon ctl reload?
# Systemctl enable
# Systemctl start

cd /usr/local/bin/
wget "https://github.com/Ryand833/rpistuff/releases/download/v0.3/buttonboot.py"
chmod 0755 buttonboot.py
cd /lib/systemd/system/
wget "https://github.com/Ryand833/rpistuff/releases/download/v0.3/buttonboot.service"
chmod 0644 /lib/systemd/system/buttonboot.service
systemctl daemon-reload
systemctl enable buttonboot.service
systemctl start buttonboot.service
