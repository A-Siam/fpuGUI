#!/usr/bin/env python3
import sys ,struct
'''
	NAME
				bi - binary input
	SYNOPSIS
				fi number [option]
	DESCRIPTION
				a simple imparative script to convert binary input in TK to float number 
				to be used in Tk
	USAGE
				./bo hex
				5.5


'''
#s =sys.argv[1]
#f_inhex = bytes(s,'utf-8') 
#\ = hex(int(sys.argv[1],2))
#print(f_inhex)
#print(sys.argv[1])
dummy = bytes.fromhex(sys.argv[1])
# print(bytes.fromhex(h[2:10]))
f = (struct.unpack('>f',dummy)[0])
print (round(f,ndigits=6))
