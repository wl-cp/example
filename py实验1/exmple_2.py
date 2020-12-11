print("**************猜年龄小游戏************")
age = 23
t = 0
while t < 3:
    t+=1
    year = input("请输入你猜的年龄:")
    temp = int(year)
    if temp > age:
        print("大啦大啦")
    elif temp < age:
        print("小啦小啦")
    else:
        print("恭喜你猜中了")
        break
else:
    print("游戏结束!")
    
    
    
    
    
  
        

