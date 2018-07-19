# Author:Jim Dai
name = input("name:")
age = int(input("age:"))
print(type(age))  # 打印变量的数据类型
job = input("job:")
salary = input("salay:")

# 格式化写法1
info = '''
----- info1 of %s-----
Name:%s
Age:%d
Job:%s
Salary:%s
------------------- 
''' % (name,name,age,job,salary)
print(info)

# 格式化写法2
info2 = f'''
----- info2 of {name}-----
Name:{name}
Age:{age}
Job:{job}
Salary:{salary}
------------------- 
'''
print(info2)

# 格式化写法3
info3 = '''
----- info3 of {0}-----
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
------------------- 
''' .format (name,age,job,salary)
print(info3)

# 格式化写法4
info4 = '''
----- info4 of {_name}-----
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
------------------- 
''' .format (_name = name ,
             _age = age,
             _job = job,
             _salary = salary)
print(info4)
