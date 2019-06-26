# It is no longer possible to use a Raspberry Pi 2/3 for SolarCoin, the RAM requirements of the blockchain have exceeded 1GB, however Raspberry Pi 4 may work, try 4GB version for maximum longevity

# Headless-SolarCoin-Raspberry-Pi-Node
Instructions to build a SolarCoin full node on Raspberry Pi, for future proofing SBCs with higher RAM may be needed, for a Rock64 install see https://github.com/jegb/solarcoin-legacy/wiki/Rock64-node

PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH USE OR OTHER DEALINGS.

1 - THIS GUIDE ONLY WORKS ON RASPBIAN STRETCH

You will need to be able to open the command line Terminal either using a screen on the HDMI port with a keyboard and mouse, or via SSH.  The guide will compile a version of SolarCoin that can only be controlled via the command line.

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

> sudo apt-get install autoconf libevent-dev libtool libssl1.0-dev libboost-all-dev libminiupnpc-dev libdb-dev libzip-dev libdb5.3++ libdb5.3++-dev git rng-tools -y

We installed rng-tools to give us really good random number generation entropy, we just need to make one change to the configuration file

> sudo nano /etc/default/rng-tools

In the file uncomment (remove the # symbol) from this line

HRNGDEVICE=/dev/hwrng

CTRL+X, Enter & Y to save

> sudo reboot  

** If you are on SSH you will lose connection, log back in to continue **

5- Clone the SolarCoin Github, compile and install the client / node with following commands:

> cd

> git clone https://github.com/solarcoin/solarcoin-legacy.git

> cd solarcoin-legacy

> git checkout compile-revisions

NOTE: ** This will create a new directory /home/pi/solarcoin-legacy **

> cd src

> sudo make -f makefile.unix -e PIE=1

NOTE: ** This is going to take a long time, go and make a cup of tea **

> sudo strip solarcoind

> sudo install -m 755 solarcoind /usr/local/bin/solarcoind

> cd

6- Start the SolarCoin daemon with:

> solarcoind

NOTE  ** This will auto-create a new directory  /home/pi/.solarcoin  which will contain your wallet.dat and blockchain files **

NOTE  ** This is not the same as                /home/pi/solarcoin   that was created in step 5 **

NOTE  ** When executing the next commands be careful to use the right one **

NOTE  ** If you connected via SSH you may need to close the terminal and login again **


7- You may get a warning and need to create a solarcoin.conf file, don’t worry:

> cd .solarcoin

> sudo nano solarcoin.conf

Enter the following:

> addnode=162.243.214.120

> addnode=139.162.244.34

> addnode=88.198.92.47

> addnode=solarhost.ddns.net

> addnode=nlsolarcoin.ddns.net

> addnode=94.124.215.192

> server=1

> daemon=1

> rpcuser=solarcoinrpc

> rpcpassword=        ** enter a secure password **

> listen=1            ** if you want a fullnode that listens for connections, you will need to enable port forwarding on your router on port 18188 as we have not complied for UPNP **

Hit CTRL+X, Y and Enter to save the file:

> cd

> solarcoind

8- To check if SolarCoin is running:

> solarcoind getinfo

NOTE  ** If you see error: couldn't connect to server, don’t worry, it just means the program is still starting up, keep trying every 30 seconds until it works **

9- OPTIONAL: Move the blockchain/wallet to a USB drive, recommended to reduce wear on the SD card:

NOTE  ** Users with a distro that has a desktop, you may find that when you insert a USB drive, this is automatically mounted, probably somewhere in /media, you may want to look at lpninjas instructions in https://github.com/Scalextrix/SolarCoin-Raspberry-Pi-Node/blob/master/StorageonUSBforROKOS.md as a better guide for this section **

Insert a USB drive, then:

> solarcoind stop

> cd /media

> sudo mkdir disk1

> sudo fdisk -l      

** find an entry like /dev/sda1, could be different on your device **

> sudo mount /dev/sda1 disk1

> cd

> sudo nano /etc/fstab

Add the following underneath the rows already present:

> /dev/sda1       /media/disk1          auto    defaults          1       2

Hit CTRL+X to save, Y to confirm and Enter

> mv .solarcoin /media/disk1

> ln -s /media/disk1/.solarcoin .solarcoin

> solarcoind

10- IMPORTANT: Encrypt and back up your wallet and keep it on at least one other device!

> solarcoind encryptwallet   **enter your secure passphrase here**

** NOTE: Never lose your passphrase or all your coins are lost, forever!  Never share your passphrase with anyone or they can steal your coins! Longer passphrases are more secure**

> solarcoind walletpassphrase **enter your secure passphrase here** 9999999


Insert (another if you followed option 9) USB drive:

> sudo mkdir /media/usb

> sudo fdisk -l

** find an entry like /dev/sdb1, could be different on your device **

> sudo mount /dev/sdb1 /media/usb

> solarcoind backupwallet /home/pi/wallet.dat

> sudo mv wallet.dat /media/usb/wallet.dat  ** you will see this message, dont worry "mv: failed to preserve ownership for ‘/media/usb/wallet.dat’: Operation not permitted" **

> sudo umount /dev/sdb1

Remove the USB drive

11- Run SolarCoin as a service, this will ensure proper shutdown and startup, and will restart SolarCoin in case of failure

> solarcoind stop

> sudo nano /etc/systemd/system/solarcoind.service

Enter the following in the file:

> [Unit]

> Description=SolarCoin daemon services

> After=tlp-init.service

>

> [Service]

> Type=forking

> PIDFile=/home/pi/.solarcoin/solarcoind.pid

> RemainAfterExit=yes

> ExecStart=/usr/local/bin/solarcoind

> Restart=on-failure

> RestartSec=3

> User=pi

> 

> [Install]

> WantedBy=multi-user.target

CTRL X, Y and Enter to save

> sudo systemctl enable solarcoind.service

> sudo systemctl start solarcoind.service

> systemctl status solarcoind.service

You should see an enabled service with a 'PID' number

That is it; you now have a SolarCoin node on your Raspberry Pi.  You need to wait for the block-chain to sync, this may take several days!  If you forget a command 

> solarcoind help 

is useful, or see https://github.com/Scalextrix/SolarCoin-Raspberry-Pi-Node/blob/master/Useful-SolarCoin-Daemon-Commands.md

** Once the block-chain is synced, its advisable to keep regular backups (I do mine monthly) of the SD card image, in this way if you have a hardware or software problem you will be able to get back up and running quickly without re-installing everything, here is a guide:  https://lifehacker.com/how-to-clone-your-raspberry-pi-sd-card-for-super-easy-r-1261113524 **

Any tips to my SLR address: 8cESoZyjFvx2Deq6VjQLqPfAwu8UXjcBkK   Thanks
