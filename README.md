# Useful files for installing and controlling a SolarCoin node on Raspberry Pi or other SBC (Single Board Computer)

After reading the installation guide (Create-a-Pi-Node.md) you should read Useful-SolarCoin-Daemon-Commands.md

You may wish to download solarcoin_RPC.py to make using the solarcoin daemon easier.

Dependencies: requests

On a Raspberry PI:

> sudo apt-get install python-requests

> git clone https://github.com/Scalextrix/SolarCoin-Raspberry-Pi-Node

> cd SolarCoin-Raspberry-Pi-Node

> sudo chmod +x solarcoin_RPC.py

> ./solarcoin_RPC.py


For a Windows machine you should install Python 2.7 https://www.python.org/downloads/release/python-2714/.

Once installed you will need to get Python requests, you may want to install pip if its not part of the python install.

> python -m pip install requests

Then download the .zip archive, extract and execute solarcoin_RPC.py
