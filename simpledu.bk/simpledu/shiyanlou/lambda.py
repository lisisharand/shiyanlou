from math import pi
def f(a):
	return lambda:a**2*pi#anonymous function
if __name__ =='__main__':
	print(f(2))
	print(f(2)())

