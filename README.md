# SBC-Kiosk
This repository houses the code for implementing a Kiosk in a Single Board Computer (SBC) such as a Raspberry Pi.

The software expects there to be physical buttons which are attached to the SBC's General Purpose Input Output (GPIO) header. Firefox must be set up to autolaunch in Kiosk mode (no toolbars or other user access) with JavaScript enabled and configured to open the Kiosk's start page. It is up to the implementer to configure the system to lock malicious users out and prevent them from plugging in unauthorized input devices. The Kiosk's start page can be placed in the local file system unless it uses server-side execution. A network of Kiosks may be easiest to administer if each Kiosk can access a central web site, but then all the Kiosks would be unusable if the network goes down. Another option is to use something like `rsync` to automatically refresh the local copy of the Kiosk screens so a single central update can propogate to a network of Kiosks but they will still work if the network is down.

## Files
### kiosk.py
The input handler of this project listens for button press events and simulates a keypress event as if the user had pressed a particular key on the keyboard. Each physical button's pin number needs to be mapped to a keyboard press event in this file. This must be set to launch automatically when the Kiosk starts, along with Firefox. It can run as a systemd process or any other mechanism as long as one (and only one) instance of it is running at all times. If you want LEDs to react when a physical button is pressed, this is where you would likely put that code as well.
### kiosk.js
The JavaScript event handler in this file forces Firefox to navigate to a different page depending on which keypress event was received. The keypress events must corrospond to the events in `kiosk.py` and are probably easiest if they are simple alphabet characters or numbers.
### kiosk.css
This is the style sheet for the webpages which is used to unify the appearance of the Kiosk screens. It can be customized or replaced entirely and is unessential to this project.
### screen1.htm and screen2.htm
These are example HTML files demonstrating how a Kiosk screen loads `kiosk.js` and acts as the primary user interface for end-users. The filenames do not have to conform to any special naming scheme on account of the kiosk. They are only named the way they are to make it clear that these are the types of files which are being referred to as "Kiosk screens."
