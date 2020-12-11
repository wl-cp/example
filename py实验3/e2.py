from random import random
import math
times = int(input('请输入投掷飞镖次数'))
hit = times
number = 0
while hit != 0:
    hit -= 1
    x = random()
    y = random()
    s = math.sqrt(x**2 + y**2)
    if s <= 1:
        number +=1
PI = number/times *4
print(PI) 


