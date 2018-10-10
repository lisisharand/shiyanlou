#! /usr/bin/env python3
filename = input("Enter file path:")
try:
	f = open(filename,'r')

	for i in f:
		print(i)
	f.close()
except FileNotFoundError:
	print("File not found")
finally:
	print("finally")
	
