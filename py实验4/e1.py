n =int(input("请输入总数："))
k =int(input("报到第几个退出："))
def josephus(n,k):
    #n代表总人数，k代表报数的数字
    List = list(range(1,n+1))
    index = 0
    while List:
        temp = List.pop(0)
        index += 1
        if index == k:
            index = 0
            continue
        List.append(temp)
        if len(List)==2:
            print(List)
            break
josephus(n,k)
    