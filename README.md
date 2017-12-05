# Useful files for installing and controlling a SolarCoin node on Raspberry Pi or other SBC (Single Board Computer)

After reading the installation guide (Create-a-Pi-Node.md) you should read Useful-SolarCoin-Daemon-Commands.md

You may wish to download solarcoin_RPC.py to make using the solarcoin daemon easier.

Dependencies: requests

The solarcoin.conf file must have the following entries:
> rpcuser=(insert a username if one isnt already present)
> rpcpassword=(insert a password if one isnt already present)
> daemon=1
> server=1

On a Raspberry PI:

> sudo apt-get install python-requests

> git clone https://github.com/Scalextrix/SolarCoin-Raspberry-Pi-Node

> cd SolarCoin-Raspberry-Pi-Node

> sudo chmod +x solarcoin_RPC.py

> ./solarcoin_RPC.py


For a Windows machine you should install Python 2.7 https://www.python.org/downloads/release/python-2714/.

Once installed you will need to get Python requests,  to make installing easier you may want to install pip if its not part of the python install.  Once done you can get requests as follows:

> python -m pip install requests

Then download the .zip archive, extract and execute solarcoin_RPC.py
