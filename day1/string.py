# Author:Jim Dai
##age = input("type in your age :")
#if age.isdigit():
#	print(int(age))
#else:
#	print("please input a number!")

name = "daijin"

print(name.capitalize())
print(name.count("a"))  #检查字符串中字母a的个数
print(name.count("i"))

name = "haha"
print(name.count("ha"))

print(name.center(50,"-")) # 将name字符串的值插入50个-中间，即前后各25个

print(name.endswith("haas")) #j检查字符串是否以haas结尾，次数结果位false

name ="hello\tworld"
print(name.expandtabs(tabsize=30))  #讲tab键转成30个空格

name = "hello world"
print(name.find("w"))     # w在字符串中首次出现的位置，此处为6
print(name[name.find("w"):11])  # 字符串切片，将取第6至第11位，将world取出

name = "my name is {name} and I am {age} years old"
print(name.format(name="daijin",age=27))
print(name.format_map( {'name':'daijin','age':27} ))  #使用字典

print("ab123".isalnum())  # 检查是否包含英文和数字
print("12".isalpha())      # 检测是否包含英文

print("1.23".isdecimal())    #
print('1aa'.isidentifier()) # 判断是不是一个合法的标识符（变量名），此处会返回false、

print('asb'.islower())  # 是否全为小写
print('ABC'.isupper())  # 是否全为大写

print('33.33'.isnumeric()) #全部字符都为数字时，返回正确
print('  '.isspace())  #字符串是否完全为空格
print('My Name Is'.istitle()) # 是否每个首字符都是大写

print('+'.join(['1','2','3','4']))
print('hello'.ljust(50,'*'))  # 保证字符串长50个字符，若不足则在右侧用*补齐
print('hello'.rjust(50,'*'))  # 保证字符串长50个字符，若不足则在左侧用*补齐

print('HELLO'.lower())  # 大写转小写
print('hello'.upper())  # 小写转大写

print('----')
print('\nAlex'.lstrip())  #去掉左边的换行或回车
print('----')
print('Alex\n'.rstrip())  #去掉右边的换行或回车




