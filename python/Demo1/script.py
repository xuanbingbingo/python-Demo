#!/usr/bin/python
#coding=utf-8

import sys;
import time;
import calendar;
import datetime;
import os;
#from support import heheda;
"""
这里是文件的注释
"""
import math;
x = 'runoob';
sys.stdout.write(x+'\n');
print "bingo";
print x,x;
bingo = raw_input("\nPress the enter key to exit.");
print "您好，世界",bingo;
a = 2;b = 2;
if a>b :
  print 'a'
elif a<b :
  print 'b'
else :
  print 'a==b'
print sys.argv;
l,m,n = 1,1.0,'hehe';
print l,m,n;

var1,var2,var3 = 1,2.0,51924361L;
del var1;
print var2,var3;
print x[0:3],x[0:],x[0],x[0] + 'hehe',x[0] * 2
list1 = [1, 'bingo', 2.0, 213131231123l];
print list1[0];
print list1[0:2];
print list1 * 2;
print list1 + list1;
xx = ('12345', 2 ,3, -5, ['1','2']);
yy = '1234,5';
ll = list(xx);
print ll;
print len(list(yy));
for name in xx: print name;
abc = (50,);
print abc[0];
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict.clear();
print dict;
ticks = time.time();
print "当前时间戳为：",ticks;
localtime = time.localtime(time.time());
print "本地时间为：", localtime;
localtime = time.asctime(time.localtime(time.time()))
print "本地时间为：", localtime;
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
cal = calendar.month(2016, 1)
print "输出2016年一月分的日历："
print cal;
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

def printme( str ):
  print str;
  return;
printme("这是测试一个函数的执行")

def printll(name, age = 10):
  print name,age;
  return;
printll(age=25, name="libin");
globvar = 0

def set_globvar_to_one():
    # 使用 global 声明全局变量(函数内只有通过global声明的全局变量，才可以更改全局变量的值，否则只是更改了局部变量的值)
    global globvar
    print(globvar)
    globvar = 3
    hehe = 2
    print(globvar)
    print(globals())
    print(locals())

def print_globvar():
    print(globvar)     # 没有使用 global

set_globvar_to_one()
print  globvar        # 输出 1
print_globvar()
#heheda("libinheheda")
print ['1','2','3']+['3']
print dir(math);
print "abc",vars();

fo = open("support.py","r");
fo.close()
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

fo1 = open("foo.txt", "wb")
fo1.write( "www.runoob.com!\nVery good site!\n");
fo1.close()

fo2 = open("foo.txt", "r+")
str1 = fo2.read(10);
print "读取的字符串是 : ", str1
# 关闭打开的文件
fo2.close()

print os.getcwd()
#os.rename("foo.txt","foooo.txt")#重命名
#os.remove("test2.txt")
#os.mkdir("newdir")
os.chdir("./newdir")
print os.getcwd()

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()


class Employee:
    empCount = 0

    def __init__(self, name, salary):
        #hehedahda
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary
emp1 = Employee("libin1", 100);
emp1.displayCount();
emp1.displayEmployee();

emp2 = Employee("libin2", 200);
emp2.displayCount();
emp2.displayEmployee();

print getattr(emp1, 'name')
print hasattr(emp1, 'name')
#setattr(emp1, 'age', 8)
#delattr(empl, 'age')
print __name__;
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__


#self代表类的实例，而非类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
        print(self.__class__.__name__)
t = Test()
t.prt()









