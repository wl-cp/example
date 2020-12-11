import math     
def prime(n):
    func = lambda x: [x%i for i in range(2, int(math.sqrt(x)) + 1) if x%i ==0]
    return filter(func, range(2,n+1))
n = int(input("请输入一个比2大的数:"))
print(list(prime(n)))
