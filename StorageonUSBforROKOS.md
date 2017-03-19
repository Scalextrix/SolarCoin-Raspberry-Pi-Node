Guide by @lpninja 
Date: 2017/03/15

PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH USE OR OTHER DEALINGS.

**USB Mounting Guide** (for solarcoin blockchain storage on a USB device) for those running ROKOS (Jessie v8 based Cryptocurrency specialised variant Linux Jessie 8 OS for Raspberry Pi devices)
Some people may want to run this variant image because it has been specialised to run coins on IoT hardware.
**Note please make sure to follow @scalextrix guidelines to compile your daemon (steps 1-8 first) and instead of doing the symlink procedure if you are on this Linux distro, you must follow this below mentioned method

This is for ROKOS v4.1.19-v7+

To find out your version of Linux in command-line:

>$cat /etc/*-release
>uname -r


1) Insert a clean new USB drive into your RPI3b
ROKOS is a Jessie 8 variant and it has auto mounting of the USB drive.

2) Note the folder by checking:


>$cd /media/usb


3) Backup your wallet.dat
4) Go to:

>$ cd /home/pi


5) Open:


>$ cd .solarcoin/


6) Update the solarcoin.conf by:

>$vi solarcoin.conf
 
then add the line


>datadir=/media/usb/solarcoin


Press ESC and type :wq (you will see it written in the bottom) and hit ENTER.

7) Go to:

>$cd /media/usb

8) Make directory:

>$mkdir solarcoin

9) Check it's there in:

>$ /media/usb

type:

>$ ls

A solarcoin directory should be found as such:

>$ /media/usb
>solarcoin

10) Go to: 

>$ cd /home/pi/.solarcoin

11) Copy to move these folders to the USB device:

>$ cp -Rf* /media/usb/solarcoin/

After making sure everything is copied overs you need to delete solarcoin.conf from /media/usb/solarcoin/

>$cd /media/usb/solarcoin/
>$rm solarcoin.conf

12) Go back to /home/pi/.solarcoin and remove everything EXCEPT solarcoin.conf

>$rm -R database
>$rm db.log
>$rm debug.log
>$rm peers.dat
>$rm -R txleveldb
>$rm wallet.dat**

**---Please make sure you have a backup either in another zip folder or USB

Check what's inside /home/pi/.solarcoin

>$ls -a

It would appear something like this in: /home/pi/.solarcoin:

>. .. .lock solarcoin.conf

12) Finally run the daemon

>$ cd /usr/local/bin
>solarcoind

The daemon should run out of /usr/local/bin if you haven't made the service yet.
Check it's running. Then in /home/pi/.solarcoin all of the files that you removed will get remade by running the daemon.

The active files that the daemon is using are the ones on /media/usb/solarcoin
