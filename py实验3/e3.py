num=int(input("请输入一个四位数:"))

c=num
flag = 0
while c!=6174:

    digits=list(str(c))

    digits.sort(reverse=True)#排列最大数和最小数

    if len(digits)<4:

        digits.append('0')

    a=int(''.join(digits))

    digits.reverse()

    b=int(''.join(digits))

    c=a-b
    flag += 1
    print("%d-%d=%d" %(a,b,c))
print("共进行了%d次运算"%flag)
'''def sws(l):     #将列表中数按顺序组成四位数
    y=l[0]*1000+l[1]*100+l[2]*10+l[3]
    return y
def jian(l):    #最大数-最小数
     l.sort()
     n1=sws(l)
     l.sort(reverse=True)
     n2=sws(l)
     t=(n2-n1)
     return t
def f(n):      #将四位数各位取出放入列表
    x=n//1000
    y=n//100%10
    z=n%100//10
    m=n%10
    l=[]
    l.append(x)
    l.append(y)
    l.append(z)
    l.append(m)
    return l
def jd(x):
     l=f(x)
     a=jian(l)
     i=1
     while(a!=6174):
            a=jian(f(a))
            i+=1
     if i<8:
            print(x,"最终得到6174操作次数：",i)
     else:
            print(x,"最终得到6174这个数字的操作超过7次。")
number = int(input("请输入一个四位数:"))
l=f(number)
if l[0]!=l[1] and l[0]!=l[2] and l[0]!=l[3]and l[1]!=l[2]and l[1]!=l[3]and l[2]!=l[3]:
    jd(number)
else:
    print("EEOOR，请输入四位不同的数")'''