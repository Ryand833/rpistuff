#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import subprocess
import os

gpio_buttona = 11
gpio_buttonb = 13
img_a = 'dynaberry.img'
img_b = 'magicmirror.img'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(gpio_buttona, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(gpio_buttonb, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

while True:
    if GPIO.input(gpio_buttona) == GPIO.HIGH:
        doreboot(img_a)
        break
    if GPIO.input(gpio_buttonb) == GPIO.HIGH:
        doreboot(img_b)
        break
    time.sleep(0.2)
