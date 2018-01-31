#coding=utf-8

# 第一章的内容记录

# 变量

port = 21
string = "bingo"
list = [1,2,3,4]
bool = True
yuanzu = (1,2,3,4)
dictionary = {'a':'a','b':'b'}
print "port:" + str(port) + "hehe" + string
print type(port)
print type(string)
print type(list)
print type(bool)
print type(yuanzu)
print type(dictionary)

# 字符串

banner = "Free FTP Server"
print banner.upper()
print banner.lower()
print banner.replace('e','a')
print banner.find('FTP')

#List(列表)

portList = []
portList.append(21)
portList.append(43)
portList.append(254)
portList.append(25)

print portList
portList.sort()
print portList
pos = portList.index(254)
print pos
portList.remove(254)
print portList
cnt = len(portList)
print cnt

#词典


