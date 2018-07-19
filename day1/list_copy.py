# Author:Jim Dai
import copy
names = ["4david","#bob","alex",["dj","xh"],"Amada","Charles","erik"]
names2 = names.copy()

print("-----------copy-----------")
print(names)
print(names2)

names[4] = "阿曼达"
names[3][0] = "DJ"
print(names)
print(names2)

#浅拷贝的情况下，是将1级列表的数据存入names2，而对于names中的子列表，直接调用内存中的原数据展示
#故当names中的元素和其中子列表的元素都被修改后，names2中存储的仍然是未修改的元素，但展示的子列表内容是在内存中被修改后的

print("---------deep_copy--------")
names = ["4david","#bob","alex",["dj","xh"],"Amada","Charles","erik"]
names2 = copy.deepcopy(names)

print(names)
print(names2)
names[4] = "阿曼达"
names[3][0] = "DJ"
print(names)
print(names2)

#实现浅拷贝的三种方式
namescopy=copy.copy(names)
namescopy=names[:]
namescopy=list(names)