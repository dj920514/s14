# Author:Jim Dai
balance=0
while True:
	recharge = int(input("请输入您的充值金额（退出请按0）： "))
	balance = balance+recharge
	if recharge == 0:
		print("已退出")
		exit()


	goods = [
		("茶杯",10),
		("鼠标",50),
		("电脑",6000),
		("宝马",500000)
	]
	buy_goods=[]
	while True:
		print("您当前的余额为：",balance)
		good_id = 1
		for i in goods:
			print("编号:",good_id,"\t\t","品名：",i[0],"\t\t","单价：",i[1])
			good_id+=1

		buy_id = int(input("请输入您想要购买的产品编号（退出按0）："))
		if buy_id == 0:
			print("已购买清单如下：")
			for i in buy_goods:
				print(i)
			print("余额为：",balance)
			exit()
		else:
			good_id=buy_id-1
			buy_amount=goods[good_id][1]

		if buy_amount > balance:
			print("对不起，您的余额不足!")
			print("1.继续购买请按(b)\n2.充值请按(c)\n3.退出程序请按(q)")
			select=input("请选择：")
			if select == "b":
				continue
			elif select == "c":
				break

			elif select == "q":
				print("已购买清单如下：")
				for i in buy_goods:
					print(i)
				exit()
			else:
				print("指令输入错误！")
				exit()
		else:
			print("已购买商品：",goods[good_id][0])
			buy_goods.append(goods[good_id][0])
			balance=balance-buy_amount

