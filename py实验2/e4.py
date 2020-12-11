x = int(input('请输入一个大于2的整数'))
a = set(range(2, x))
b = set()
for i in a:
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        b.add(i)
print(b)
