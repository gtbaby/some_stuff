import os
import re

names = []
name_done = []

with open('names.txt','r') as f:
	while True:
		x = f.readline()
		if x:
			names.append(x.strip())
		else:
			break

for file in os.walk('.\\files'):
	file = file[2]

for i in file:
	#num = re.sub(r'\D', "", i)
	name = re.sub(r'[^\u4E00-\u9FA5]',"", i)
	name_done.append(name)
	names.remove(name)
	#f.write(i[-15:-5])
	#f.write(',')
	#f.write(i[:-16])
print('目前提交情况：')
#print("已提交(%s人)："%(len(name_done)),name_done)
print("未提交(%s人)："%(len(names)),names)

x = input('按回车键退出')