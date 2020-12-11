import math 
   
number = int(input("请输入一个比2大的数:")) 
def prime(n):
    func = lambda x: not[x%i for i in range(2, int(math.sqrt(x)) + 1) if x%i ==0]
    return filter(func, range(2,n+1))
print(list(prime(number)))











