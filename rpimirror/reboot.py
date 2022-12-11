#!/usr/bin/env python3
import time
import subprocess
import os
import socket

img_a = 'Dynaframe.img'
img_b = 'MagicMirror.img'
hostname_a = 'DynaframePro'
hostname_b = 'raspberrypi'

def doreboot(image):
    if not(os.path.exists('/mnt/berrydata')):
        os.makedirs('/mnt/berrydata')
    p = subprocess.Popen('mount /dev/mmcblk0p2 /mnt/berrydata', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    rcode = p.returncode
    f = open('/mnt/berrydata/data/default', 'w')
    f.write(image)
    f.close()
    p = subprocess.Popen('umount /mnt/berrydata', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    rcode = p.returncode
    os.system('reboot')

this_host = socket.gethostname()
image = img_a
if this_host == hostname_a:
    image = img_b
doreboot(image)
