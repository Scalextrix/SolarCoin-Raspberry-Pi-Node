#!/usr/bin/env python

"""solarcoin_RPC.py: simple interface for contolling a commandline solarcoind or solarcoin-qt,
on local or remote Windows or Linux devices.  Note this is not secure, do not use outside of LAN"""

__author__ = "Steven Campbell AKA Scalextrix"
__copyright__ = "Copyright 2017, Steven Campbell"
__license__ = "The Unlicense"
__version__ = "1.0"

import getpass
import json
import os
import requests
import sys
import time

def command_chooser():
	command_choice = raw_input('Issue a command, "help" or "exit" to exit: ').lower()
	if command_choice == 'lock':
		return lock_wallet()
	elif command_choice == 'send':
		return send()
	elif command_choice == 'staking':
		return staking_wallet()
	elif command_choice == 'unlock':
		return unlock_wallet()
	elif command_choice == 'blocks':
		return blocks()
	elif command_choice == 'info':
		return info()
	elif command_choice == 'stakinginfo':
		return stakinginfo()
	elif command_choice == 'balance':
		return balance()
	elif command_choice == 'help':
		print 'Here is the list of available commands:'
		print ''
		print 'Type "help" for this help'
		print ''
		print 'Type "lock" to lock the wallet'
		print ''
		print 'Type "unlock" to unlock the wallet: you will subsequently be asked for the passphrase and number of seconds'
		print '*TIP: you may need to LOCK the wallet if it is already UNLOCKED for STAKING*'
		print ''
		print 'Type "send" to send funds: you will need to know the wallet address and amount'
		print '*TIP: you will need to UNLOCK first if the wallet is LOCKED or UNLOCKED for STAKING'
		print ''
		print 'Type "staking" to indefinately unlock the wallet for staking: you will subsequently be asked for the passphrase'
		print '*TIP: you may need to LOCK the wallet if it is already UNLOCKED*'
		print ''
		print 'Type "blocks" to see the current number of blocks this node has'
		print ''
		print 'Type "info" to see basic information about your node'
		print ''
		print 'Type "balance" to see the total SLR in your wallet'
		print ''
		print 'Type "stakinginfo" to see if this node is staking'
		print '*TIP: if this node is staking the output should read Enabled: true and Staking: true'
		print '**TIP: If Enabled: false then Type "staking" to UNLOCK for STAKING'
		print '***TIP:: If Staking: false then check if you are fully synced to the blockchain, Type "blocks"'
		print ''
		return command_chooser()
	elif command_choice == 'exit':
		print 'Exiting'
		time.sleep(10)
		sys.exit()
	else:
		print 'Command not recognised, perhaps use "help" for list of available commands'
		return command_chooser()

def blocks():
	method = "getblockcount"
	params = []
	modifier = ""
	return {'method':method, 'params':params, 'modifier':modifier}

def balance():
	method = "getinfo"
	params = []
	modifier = "balance"
	return {'method':method, 'params':params, 'modifier':modifier}

def info():
	method = "getinfo"
	params = []
	modifier = ""
	return {'method':method, 'params':params, 'modifier':modifier}
        
def stakinginfo():
	method = "getstakinginfo"
	params = []
	modifier = ""
	return {'method':method, 'params':params, 'modifier':modifier}

def instruct_wallet(ip_choice, command, command_chooser):
	payload = json.dumps({"method": command['method'], "params": command['params']})
	headers = {'content-type': "application/json", 'cache-control': "no-cache"}
	try:
		response = requests.request("POST", url, data=payload, headers=headers, auth=(rpc_user, rpc_pass))
	except requests.exceptions.RequestException as e:
		print e
		time.sleep(10)
		sys.exit()
	answer = json.loads(response.text)
	if answer['error'] == None:
		print 'Command Executed Successfully!'
		if command['method'] == 'getinfo' and command['modifier'] == 'balance' and answer['result'] != None:
			print '{'
			print '"balance": {},'.format(json.dumps(answer['result']['balance']))
			print '"stake": {},'.format(json.dumps(answer['result']['stake']))
			print '"total": {}'.format(float(json.dumps(answer['result']['balance']))+float(json.dumps(answer['result']['stake'])))
			print '}'
		elif answer['result'] != None:
			print json.dumps(answer['result'], sort_keys=True, indent=4, separators=(',', ': '))
	else:
		print answer['error']['message']
	command = command_chooser()
	return instruct_wallet(ip_choice, command, command_chooser)

def lock_wallet():
	method = "walletlock"
	params = []
	modifier = ""
	return {'method':method, 'params':params, 'modifier':modifier}

def send():
	method = "sendtoaddress"
	address = raw_input('Send SLR to which address: ')
	amount = float(raw_input('How much SLR to send: '))
	params = [address, amount]
	modifier = ""
	return {'method':method, 'params':params, 'modifier':modifier}

def staking_wallet():
	passphrase = getpass.getpass(prompt="What is your SolarCoin Wallet Passphrase: ")
	method = "walletpassphrase"
	params = [passphrase, 9999999, True]
	modifier = ""
	return {'method':method, 'params':params, 'modifier':modifier}

def unlock_wallet():
	passphrase = getpass.getpass(prompt="What is your SolarCoin Wallet Passphrase: ")
	unlock_time = int(raw_input('unlock for how many seconds: '))
	method = "walletpassphrase"
	params = [passphrase, unlock_time]
	modifier = ""
	return {'method':method, 'params':params, 'modifier':modifier}

if os.name == 'nt':
	user_account = getpass.getuser()
	f = open('C:\Users\{}\AppData\Roaming\SolarCoin\SolarCoin.conf'.format(user_account), 'rb')
	for line in f:
		line = line.rstrip()
		if line[0:7] == 'rpcuser':
			rpc_user = line[line.find('=')+1:]
		if line[0:11] == 'rpcpassword':
			rpc_pass = line[line.find('=')+1:]
	f.close()
elif os.name == 'posix':
	homedir = os.environ['HOME']
	f = open(homedir+'/.solarcoin/solarcoin.conf', 'r')
	for line in f:
		line = line.rstrip()
		if line[0:7] == 'rpcuser':
			rpc_user = line[line.find('=')+1:]
		if line[0:11] == 'rpcpassword':
			rpc_pass = line[line.find('=')+1:]
	f.close()
else:
	print 'SolarCoin.conf not found'
	time.sleep(10)
	sys.exit()

ip_choice = raw_input('What is the IP address of the wallet to control (leave blank for local machine): ')
if ip_choice == '':
	ip_choice = '127.0.0.1'    
url = "http://"+ip_choice+":18181/"

command = command_chooser()
instruct_wallet(ip_choice, command, command_chooser)
