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

p = str.maketrans("abcdef","123456")  # 定义一组对应关系p
print("dai".translate(p))               #  以p所定义的关系对dai进行转换

print('daijin'.replace('i','I',1))      # 替换，将i替换为I，最后一位表示替换几个
print('daijin'.rfind('i'))      # 从左往右，找到最右侧i的下标，0为起始位
print('1+2+3+4'.split('+'))     # 将1+2+3+4，以+号分隔为列表
print('hello\nworld'.splitlines()) # 按照换行符来分隔列表

print('DaiJin'.swapcase())  #大小写互换
print('dai jin'.title())    #首字母大写，空格后也是
print('12'.zfill(4))        # 左侧补零填充，共4位




