#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import subprocess
import os

gpio_button = 11
gpio_switch = 13
img_a = 'dynaberry.img'
img_b = 'magicmirror.img'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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



while False:
    if GPIO.input(gpio_button) == GPIO.HIGH:
        print("Button was pressed!")
        switch_pos = 'a'
        image = img_a
        if GPIO.input(gpio_switch) == GPIO.HIGH:
            switch_pos = 'b'
            image = img_b
        print("Switch position: " + switch_pos)
        doreboot(image)
        break
    time.sleep(0.2)
