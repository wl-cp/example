print("IBM计算")
height = input("请输入身高：")
whight = input("请输入体重：")
h = float(height)
w = float(whight)
bmi = w/(h**2)
if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 25:
    print("体重正常")
elif 25 <= bmi < 28:
    print("体重过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
