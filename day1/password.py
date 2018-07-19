# Author:Jim Dai
import getpass

_username = 'dj'
_password = 'abc123'


username = input("username:")
password = getpass.getpass("password:")

if _username == username and _password == password:
	print("Welcome user {name} login" .format(name=username))
else:
	print("Wrong username or password!")

