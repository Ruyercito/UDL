#!/usr/bin/env python3

import sys, os, traceback, optparse
import time, datetime
import socket, struct

# PACKAGE TYPE REGISTER #
REG_REQ = 0X00
REG_INFO = 0X01
REG_ACK = 0X02
INFO_ACK = 0X03
REG_NACK = 0X04
INFO_NACK = 0X05
REG_REJ = 0X06

# ALIVE PACKAGE TYPE REGISTER #
ALIVE = 0X10
ALIVE_REJ = 0X11

# STATUS TYPE REGISTER #
DISCONNECTED = 0XA0
NOT_REGISTERED = 0XA1
WAIT_ACK_REG = 0XA2
WAIT_INFO = 0XA3
WAIT_ACK_INFO = 0XA4
REGISTERED = 0XA5
SEND_ALIVE = 0XA6
status = NOT_REGISTERED

# DATA TRANSFER PACKAGE TYPE REGISTER #
SEND_DATA = 0X20
SET_DATA = 0X21
GET_DATA = 0X22
DATA_ACK = 0X23
DATA_NACK = 0X24
DATA_REJ = 0X25

# LOOP VARIABLES REGISTER #
t = 1
u = 2
n = 7
o = 3
p = 3
q = 3
break_loop = 0

def print_debug(message):
	if strcmp(argv[i], "-d") == 0:
		print_time()
		printf(message)

def print_time():
	time(timer)
	tm_info = localtime(timer)

	strftime(buffer, 26, "%H: %M: %S", tm_info)
	printf(buffer)

def read_client_configuration(file):
	for i in range(0, 13):
		package_id[i] = '\0'

	for i in range()



def send_udp_message(package):
	if sendto(sock_udp, package, 84, 0, server_addr, sizeof(server_addr)) < 0:
		print_debug("Sending error\n")
	if package[0] == REG_REQ:
		print_debug("REG_REQ has been sent\n")
	elif package[0] == ALIVE:
		print_debug("ALIVE package has been sent\n")
	else:
		print_debug("Bad type of package has been sent\n")

def create_package(package_type, data):
	result = malloc(84)
	result[0] =  package_type

	for i in range(0, 13):
		result[i+1] = package_id[i]
	for i in range(0, 9):
		result[i+14] = random_number[i]
	for i in range(0, 61):
		result[i+23] = data[i]

	return result

def register_attempt():
	for j in range(0, 8) & (status == WAIT_ACK_REG | status == DISCONNECTED) & break_loop == 0
		if j < 1 :
			send_udp_message(create_package(REG_REQ, ""))
			if status == DISCONNECTED:
				status = WAIT_ACK_REG
				printf("State has changed from DISCONNECTED TO WAIT_ACK_REG.\n")
			recieve_udp_message(t)

