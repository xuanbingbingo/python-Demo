
#coding=utf-8

import time;
myDirectionary = {'name':'bingo','heheda':'bingo1'};

for key,value in dict.items(myDirectionary):
    print ('hehe')
    time.sleep(0.2)

print ("Values: %s" % dict.values(myDirectionary))

print (time.time());
print (time.localtime(time.time()))
print (time.strftime('%Y/%m/%d/%H:%M:%S',time.localtime(time.time())))
