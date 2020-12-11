import time
scale=50
print("执行开始".center(scale//2,"-"))
#使用字符串处理中的.center方法，讲一个“-”字符填充在执行开始
start=time.perf_counter()  #增加计时效果
for i in range (scale+1):
  a='*'*i
  b='.'*(scale-i)
  c=(i/scale)*100
  dur=time.perf_counter()-start
  #用来每一次用来打印文本进度条所用的时间，方法就是每次调用time.perf_counter()函数
  print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
  #为了使文本进度条有单行刷新效果，增加“\r”,实现光标向行首移动
  #增加end函数，把end函数赋值为空字符串，在每次输出后不换行
  time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))
#使用字符串处理中的.center方法，讲一个“-”字符填充在执行结束


#覆盖了字符串处理、数字处理以及时间库的使用等方面的内容。