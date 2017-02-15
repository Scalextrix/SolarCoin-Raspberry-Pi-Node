# SolarCoin-Raspberry-Pi-Node
Instructions to build a SolarCoin full node on Raspberry Pi

You will need to be able to open the command line Terminal either using a screen on the HDMI port with a keyboard and mouse, or via SSH.  The guide will compile a version of SolarCoin that can only be controlled via the command line.

1 - The distribution version we need to flash on the SD card is the latest Stable Raspbian Image from: https://www.raspberrypi.org/downloads/raspbian/

For instructions on how to flash an SD card: https://www.raspberrypi.org/documentation/installation/installing-images/

2- Setup Raspbian in the Pi

  a) Insert the flashed SD with Raspbian in the Raspberry Pi 2/3.

  b) Plug in the USB mouse, the USB keyboard, the HDMI screen, the network cable, and the power cable.  You may also SSH to the Raspberry Pi.

The Raspberry Pi will boot for the first time, login with user 'pi' and password 'raspberry'.

> sudo raspi-config

You will be presented with the Raspberry Pi Software Configuration Tool (raspi-config). To navigate in this tool, the useful keys are: The up/down arrow, the Enter key, and the Tab key whenever the up/down arrow keys don’t do the job. Here, we will do next things:

  b.1) Expand the Filesystem by choosing Option 1, TAB to <Finish>, and Reboot. You will get a message Root partition has been resized.  If you are on SSH your terminal may abort, if this occurs just close the session and login to the Pi again.

  b.2) Select your Proper Time Zone and Change the User Password by choosing option 2. Enter your new password twice. When entering the password, the characters won’t be displayed as a security feature. You will get a message Password changed successfully.
After reboot check the time is correct with:

> date
