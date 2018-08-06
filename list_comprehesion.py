#!/usr/bin/env python3
numbers = [1,2,3,4,5,6,7,8,9]
f = filter(lambda x:x %2 == 0,numbers)#filter() map() advanced function
m = map(lambda x:x *x ,numbers)
for i in f:
	print(i)
for k in m:
	print(k)

