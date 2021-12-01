#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import sys
import smbus

def usage():
	"""^(^_^)^"""
	print(sys.argv[0] + ' [target address] [digit]')
    
def app_main():
	"""application main procedure"""
	if len(sys.argv) < 3:
		usage()
		return
	bus = smbus.SMBus(1)

	# set pattern
	bus.write_word_data(int(sys.argv[1]), 1, 1)

	# set duration
	bus.write_word_data(int(sys.argv[1]), 2, 1000)

	# set number
	bus.write_word_data(int(sys.argv[1]), 3, int(sys.argv[2]))

	# set start
	bus.write_word_data(int(sys.argv[1]), 0, 0)

	bus.close()
    
if __name__ == '__main__':
	app_main()
