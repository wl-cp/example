
import math    
number = int(input("请输入一个比2大的数:"))
pri = set(range(2,number))
print(pri)
data = set()
for  value in pri:
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            data.add(value)
            break
data1 = pri.difference(data)
print(data1)



