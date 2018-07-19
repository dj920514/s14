# Author:Jim Dai
username = 'dj'
password = '1234'

count = 0
while count < 3:
	_username = input("请输入用户名：")
	_password = input("请输入密码：  ")

	if _username == username and _password == password:
		print("用户 {name} ,欢迎您! " .format(name = _username))
		break
	else:
		if count != 2:
			print("用户名或密码输入错误！请重试")
			count+=1
		else:
			print("尝试失败次数过多,程序退出")
			break
