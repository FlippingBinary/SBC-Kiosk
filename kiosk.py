#!/usr/bin/python

# This is designed for a Raspberry Pi, and may need 'uinput' installed for Python
# https://github.com/tuomasjjrasanen/python-uinput

# This particular code must run for the duration of time the Kiosk is expected to be used.
# Having it autostart when the Kiosk turns on is probably best.

import uinput
from gpiozero import Button
import time

# You must declare which keys you want your virtual keyboard to emulate.
device = uinput.Device([uinput.KEY_1,uinput.KEY_2])

# Wire a button to pin 2 and use it like you're pressing the number '1'
button1 = Button(2)
button1.when_pressed = lambda: device.emit_click(uinput.KEY_1)

# Wire a button to pin 17 and use it like you're pressing the number '2'
button2 = Button(17)
button2.when_pressed = lambda: device.emit_click(uinput.KEY_2)

# You can create your own button events and pick different pins than 2 or 17, so go crazy with it.


# The important thing is to stay alive and listen for button press events
# Button presses are handled in a different thread if you set them up above, so this
# script just needs to sleep indefinitely.
while 1:
  time.sleep(0.2)
