# Author:Jim Dai
#names = "alex bob crack david"
names = ["alex","bob","erik","crack","david"]
#取出alex和crack
print(names[0],names[2])

#取出中间两个（bob，crack）
print(names[1:3]) # 切片 （起始位置包含、结束位置不包含）

#取最后一个(负号代表从后往前开始数)
print(names[-1])

#取最后两个数（从后往前数，先写位于左边的下标）
print(names[-3:-1]) #由于右边为开区间不包含，故取最后两个数需要用下面的方法
print(names[-2:]) #省略掉最后的-0

#取前三个的两种写法
print(names[0:3])
print(names[:3])

#添加元素(追加)
names.append("erik")
print(names)

#添加元素（指定准确位置）
names.insert(1,"frankin") #数字为你想插入的位置
print(names)

#修改元素，将bob改为barry
names[2] = "barry" #第三位是bob，直接将其替换
print(names)
'''
#删除元素，删除frankin
#方法1（直接写要删除的元素）
names.remove("frankin")
#方法2（del 变量加下标）
del names[1]
#方法3(数字为下标，不写默认为最后一个)
names.pop(1)
'''

#查询某个元素的下标
print(names.index("barry"))

#引用下标
print(names[names.index("barry")])

#统计元素出现次数
print(names.count("erik"))

#清空列表
#names.clear()
print(names)

#反转列表
names.reverse()
print(names)

#排序(排序规则：特殊符号、数字、大写字母、小写字母)
names.sort()
print(names)

#并入（新定义一个列表names2，将其并入names）
names2 = [1,2,3,4]
names.extend(names2)
print(names)

#删除列表
del names2
print(names2)