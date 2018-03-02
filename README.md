# Useful files for installing and controlling a SolarCoin node on Raspberry Pi or other SBC (Single Board Computer)

If you use the GUI-Create-a-Pi-Node.md you dont need this set of instructions.

However if you want a headless node and use Create-a-Pi-Node-Headless.md you can read Useful-SolarCoin-Daemon-Commands.md

You may wish to download solarcoin_RPC.py to make using the solarcoin healess version easier, if so:

Dependencies: requests

The solarcoin.conf file must have the following entries:
> rpcuser=insert_a_username_if_one_isnt_already_present

> rpcpassword=insert_a_password_if_one_isnt_already_present

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
