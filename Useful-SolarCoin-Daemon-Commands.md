PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN 
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH USE OR OTHER DEALINGS.

Once you have your SolarCoin daemon running on an IoT device like a Raspberry Pi, you might 
need a little help understanding how to use it.

# The Basics

To start the SolarCoin daemon:
> solarcoind

To stop the SolarCoin daemon:
> solarcoind stop

If you followed Section 11 and created a service, you may also:
> sudo systemctl start solarcoind.service

and 
> sudo systemctl stop solarcoind.service

This is useful if you wanted to disable the service (for example if you wanted to prevent SolarCoin starting at power on)
> sudo systemctl disable solarcoind.service

And to enable it again
> sudo systemctl enable solarcoind.service

# General Monitoring

There are some useful commands to monitor your wallet:
> solarcoind getinfo

This is a great general purpose query, it tells you most things like the software version, how 
many coins you have spendable and how many are staking, how many blocks your node is sync'd to
and how many peers you are connected to, what your IP address is and whether your wallet is 
unlocked.

However its quite hard to read when you are new, so some more targeted queries may be useful:
> solarcoind getblockcount

Unsurprisingly tells you how many blocks your node is synchronized with.  You need to be sync'd 
with the blockchain before spending coins or staking coins (receiving coins is unaffected).

> solarcoind getpeerinfo

Tells you more about the connections you have to peers on the network, if they are incoming or 
outgoing.

> solarcoind getstakinginfo

Tells you if your wallet is unlocked for staking (see below) and if it is actually staking 
(both the "Enabled" and "Staking" entries should be 'true'), a reason you may be unlocked for staking ("Enabled" : true) but not actually staking ("Staking" : false) is if you are not sync'd to the blockchain.

> solarcoind getbalance

Shows you your AVAILABLE (Spendable) balance, if the amount seems too low note that any amounts 
that are locked due to them staking are not shown. 
If you arent sure use 'solarcoind getstakinginfo' to see if there is an amount of coins in the stake 
amount.  In the Receiving SolarCoin section below there is more info on checking/repairing the wallet.



# Wallet; Locked, Staking, Unlocked

In the tutorial we used 'solarcoind encryptwallet your_passphrase_here' to secure the wallet with 
a passphrase, this is to prevent anyone except for you, from controlling your wallet.
When you start solarcoind, your wallet is always locked, this means you cant send coins anywhere, 
nor can you earn additional rewards by staking your coins.  If you wanted to send me 1 SolarCoin 
(please dont feel obliged, its just an example!) you need to take multiple steps, first unlock the 
wallet:

> solarcoind walletpassphrase your_passphrase_here 300

Lets disect that for a moment; 'solarcoind' is the way to issue any command to SolarCoin, 
'walletpassphrase' tells the wallet you want to unlock the wallet, 'your_passphrase_here' is 
whatever you chose as your passphrase, '300' is the number of seconds to unlock the wallet for,
after which it will become locked again.  You can do any number of seconds, 300 is plenty for most scenarios.

So now you have 5 minutes (300 seconds) to issue the send coins command.  To send the coins:
> solarcoind sendtoaddress 8cESoZyjFvx2Deq6VjQLqPfAwu8UXjcBkK 1

Lets disect that for a moment; 'solarcoind' to send the instruction, 'sendtoaddress' to tell the 
wallet you want to send coins, '8cESoZyjFvx2Deq6VjQLqPfAwu8UXjcBkK' is my wallet address, '1' is the
amount of SLR to send.  When you hit return you will get a long string of numbers and letters, this
is the transaction hash and lets you know it worked.  Also you could message me with the transaction hash and I
could see that you had sent the coins; useful as a proof of payment for example.

To lock a wallet:

Lets say you accidentally did:
> solarcoind walletpassphrase your_passphrase_here 30000

Now your wallet is open for a long time (30000 seconds), and for security you want to lock it again
before the time expires, just do:
> solarcoind walletlock

Thats it, 'walletlock' locks the wallet, easy.

There is an intermediate state of the wallet, that is used for staking your coins (earning 
interest on them), the wallet is unlocked, but ONLY for staking, no other transactions are allowed.
You will probably want to leave your wallet in this state most of the time to earn interest.
The command is:
> solarcoind walletpassphrase your_passphrase_here 9999999 true

Lets disect that: 'solarcoind walletpassphrase your_passphrase_here' is exacly the same as fully unlocking
your wallet to send an amount, but we have '9999999' for the seconds and 'true' at the end.  
'9999999' seconds effectively means forever, and the 'true' means unlock the wallet, but for staking only.

So lets take the scenario where your wallet is unlocked for staking, and you want to transfer me that 1 SLR,
you need to do:
> solarcoind walletlock

*(your wallet was UNLOCKED for staking, so first you must lock it)*
> solarcoind walletpassphrase your_passphrase_here 300

*(fully unlock for 5 minutes, to allow the transaction)*
> solarcoind sendtoaddress 8cESoZyjFvx2Deq6VjQLqPfAwu8UXjcBkK 1

*(send me 1 SLR)*
> solarcoind walletlock

*(lock the wallet again, or you could just wait 5 minutes)*
> solarcoind walletpassphrase your_passphrase_here 9999999 true  

*(unlock the wallet for staking again)*
> solarcoind getstakinginfo

*(just to check you are back to staking)*



# Receiving SolarCoin

Its often advisable to generate a new wallet address each time you want to receive some SolarCoin from a new person, in a completely open system, it helps hide your identity.  If you ever want a new wallet address, simply:
> solarcoind getnewaddress

If you want to see a list of existing addresses, its a bit more complicated and is really much easier in a 
Qt wallet with coin control features, but you can issue command:
> solarcoind listunspent

it will show you batches of coins, numbers of confirmations and the addresses which they are associated to, 
its not easy to read though.

Sometimes you might need to repair the wallet, the reasons for this are complex, but if you suddenly notice
your balances seem wrong you can try
> solarcoind checkwallet

or
> solarcoind repairwallet



# Backup your wallet regularly, no really, BACKUP YOUR WALLET REGULARLY!!

Finally, remember to keep regular backups of your wallet, if the SD card on your Pi fails, or if there is 
some other failure ALL YOUR SOLARCOINS COULD BE LOST FOREVER.  Therefore keep 'wallet.dat' file on at least one other offline device:
> solarcoind backupwallet /destination/directory/of/your/choice/wallet.dat
