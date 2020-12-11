import random

cjdict = {'一等奖':(0,0.05),'二等奖':(0.05,0.3),'三等奖':(0.3,1.0)}

def cjfun():
    num = random.random()   
    for key,value in cjdict.items():      
        if value[0] <= num < value[1]:
            return key

dict = {}     
number = int(input('请输入抽奖次数：'))
for i in range(number):
    result = cjfun()
    if result in dict:
        dict[result] += 1
    else:
        dict[result] = 1

print('奖项\t\t\t数量')
for k,v in dict.items():
    print('%s\t\t%s' %(k,v))