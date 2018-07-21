# Author:Jim Dai
info = {
	'stu1101': "alex",
	'stu1102': "bob",
	'stu1103': "charles",
	'stu1104': "david",
}
print(info)

#打印结果的排列和上述列出并不相同，是由于字典是无序的

print(info["stu1101"])  #按照key值stu1101查询


info["stu1101"]="埃里克" #修改key stu1101所对应的值
print(info)

info["stu1105"]="弗兰克"   #若key不存在，则为添加
print(info)

del info['stu1101']     #删除key  stu1101，以及其对应的值
info.pop("stu1102")
info.popitem()          #随机删除
print(info)

print(info.get("stu1110"))      #检查键值是否存在，有返回，没有为none，建议写法

print('stu1104' in info)    #检查键值是否存在，在py2中等同于info.has_key("1103")