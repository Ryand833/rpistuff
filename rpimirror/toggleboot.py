#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import subprocess
import os
import socket

gpio_button = 11
img_a = 'Dynaframe.img'
img_b = 'MagicMirror.img'
hostname_a = 'DynaframePro'
hostname_b = 'raspberrypi'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
while True:
    if GPIO.input(gpio_button) == GPIO.HIGH:
        image = img_a
        if this_host == hostname_a:
            image = img_b
        doreboot(image)
        break
    time.sleep(0.2)
