# Author:Jim Dai
names = ["4david","#bob","alex",["dj","xh"],"Amada","Charles","erik"]
print(names[0:-1:2])
#根据步长切片，意为取0,2,4下标的元素，类似于range(1,10,2)
#取全部时，可以写成print(names[:])，步长为2可以这么写print(names[::2])
for i in names:
	print(i)

