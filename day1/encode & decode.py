# Author:Jim Dai
msg = "你好"

print(msg)
print(msg.encode(encoding='utf-8')) #将字符型str转换为2进制型，encode时需要跟上要被转换的源的字符集
print(msg.encode(encoding='utf-8').decode(encoding='utf-8')) # 将二进制转换为字符型

