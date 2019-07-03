# It is no longer possible to use a Raspberry Pi 2/3 for SolarCoin, the RAM requirements of the blockchain have exceeded 1GB, however Raspberry Pi 4 may work, try 4GB version for maximum longevity

# Gui-SolarCoin-Raspberry-Pi-Node
Instructions to build a SolarCoin full node on Raspberry Pi, for future proofing SBCs with higher RAM may be needed, for a Rock64 install see https://github.com/jegb/solarcoin-legacy/wiki/Rock64-node

PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH USE OR OTHER DEALINGS.

1 - THIS GUIDE WORKS ON RASPBIAN STRETCH, DOWNLOADS AVAILABLE FROM https://downloads.raspberrypi.org/

You will need to be able to open the command line Terminal either using a screen on the HDMI port with a keyboard and mouse, or via SSH.  The guide will compile a version of SolarCoin that has a GUI interface via desktop environment.

For instructions on how to flash an SD card: https://www.raspberrypi.org/documentation/installation/installing-images/

2- Setup Raspbian in the Pi

  a) Insert the flashed SD with Raspbian in the Raspberry Pi 2/3.

  b) Plug in the USB mouse, the USB keyboard, the HDMI screen, the network cable, and the power cable.  You may also SSH to the Raspberry Pi.

The Raspberry Pi will boot for the first time, login with user 'pi' and password 'raspberry'.

> sudo raspi-config

You will be presented with the Raspberry Pi Software Configuration Tool (raspi-config). To navigate in this tool, the useful keys are: The up/down arrow, the Enter key, and the Tab key whenever the up/down arrow keys don’t do the job. Here, we will do next things:

  b.1) Expand the Filesystem by choosing Option 1, TAB to Finish, and Reboot. You will get a message Root partition has been resized.  If you are on SSH your terminal may abort, if this occurs just close the session and login to the Pi again.

  b.2) Select your Proper Time Zone and Change the User Password by choosing option 2. Enter your new password twice. When entering the password, the characters won’t be displayed as a security feature. You will get a message Password changed successfully.
After reboot check the time is correct with:

> date

  b.3) OPTIONAL If you don’t intend to use a display (ie you are on SSH), or output any video media we can free up additional RAM by reducing the amount dedicated to the GPU
  
> sudo raspi-config

Select Advanced Options > Memory Split

Change the entry from 64 to 16

TAB to FINISH and Reboot

b.4) OPTIONAL (not needed if using desktop): If you have a Pi3 with internal Wi-Fi on SSH and would prefer to connect to the Pi via Wi-Fi; then edit the wpa_supplicant.conf file

> sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

Add the following lines

> network={

> ssid="YOURWIFISSID"

> psk="YOURWIFIPSK"

> }

CTRL+X to save, Y to confirm and then hit Enter

> sudo reboot

Disconnect the Ethernet cable and find your new IP address in your Wi-Fi router.

3- Update the Raspberry Pi device.

Run the following commands:

> sudo apt-get update

> sudo apt-get upgrade -y

4- Setting up the Raspberry Pi for compiling SolarCoin

a- Use the following command to change the default swap size:

> sudo nano /etc/dphys-swapfile

Make sure it reads CONF_SWAPSIZE=1024 Use the left/right arrow keys to navigate the file. After change is done, press Ctrl+X followed by Y then Enter key to save the file.
Use the following commands to enable the swap file with its new size:

> sudo dphys-swapfile setup

NOTE: This may take a few minutes

> sudo dphys-swapfile swapon

You can check the new active swap size with next command:

> free -m

Reduce the 'swappiness' so as to only use SWAP when absolutely needed:

> sudo nano /etc/sysctl.conf

add 

> vm.swappiness=1 

as the last line then CTRL+X, Y and Enter to save.

b- Install Required Dependencies with next commands:

> sudo apt-get install build-essential libssl1.0-dev libzip-dev libboost-all-dev libqrencode-dev libqt5webkit5-dev qt5-qmake libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev-tools qt5-default libminiupnpc-dev libdb5.3++ libdb5.3++-dev git rng-tools -y

We installed rng-tools to give us really good random number generation entropy, we just need to make one change to the configuration file

> sudo nano /etc/default/rng-tools

In the file uncomment (remove the # symbol) from this line

HRNGDEVICE=/dev/hwrng

CTRL+X, Enter & Y to save

> sudo reboot  

** If you are on SSH you will lose connection, log back in to continue **

5- Clone the SolarCoin Github, compile and install the client / node with following commands:

> git clone https://github.com/solarcoin/solarcoin-wallet-stable

> cd solarcoin-wallet-stable

> git checkout compile-revisions

> qmake -qt=qt5

> make

NOTE: ** This is going to take a long time, go and make a cup of tea **

> sudo install -m 755 solarcoin-qt /usr/local/bin/solarcoin-qt

You are done with the terminal window, and can close it, if you are on SSH you now need to start the desktop environment.

6- Start the SolarCoin-Qt by going to the main menu and opening the Run command:

> solarcoin-qt

NOTE: Allow the wallet to sync slowly, do NOT use the block-chain snapshot

If you have any problems getting connections (you may want to do this anyway):

> cd

> nano .solarcoin/solarcoin.conf

Then add the following:

> addnode=162.243.214.120

> addnode=139.162.244.34

> addnode=88.198.92.47

> addnode=nlsolarcoin.ddns.net

> addnode=solarhost.ddns.net

> addnode=94.124.215.192

CTRL+x, then y and Enter to save, now restart solarcoin-qt

** Once the block-chain is synced, its advisable to keep regular backups (I do mine monthly) of the SD card image, in this way if you have a hardware or software problem you will be able to get back up and running quickly without re-installing everything, here is a guide:  https://lifehacker.com/how-to-clone-your-raspberry-pi-sd-card-for-super-easy-r-1261113524 **

Any tips to my SLR address: 8cESoZyjFvx2Deq6VjQLqPfAwu8UXjcBkK   Thanks
