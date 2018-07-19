# Author:Jim Dai
with open('C:/Users/test.txt','r') as f:
	print(f.read())

with open('C:/Users/test.txt','a') as f:
	f.write('Hello, world!\n')