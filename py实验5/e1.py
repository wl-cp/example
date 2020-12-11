class Operation(object):
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def add(self,another):
        x=self.x+another.x
        y=self.y+another.y
        z=self.z+another.z
        print("加法运算=（{},{},{}）".format(x,y,z))

    def sub(self,another):
        x=self.x-another.x
        y=self.y-another.y
        z=self.z-another.z
        print("减法运算=（{},{},{}）".format(x, y, z))

    def mul(self,n):
        x=self.x*n
        y=self.y*n
        z=self.z*n 
        print("乘法运算=（{},{},{}）".format(x, y, z))
        
    def truediv(self,n):
        x=self.x/n
        y=self.y/n
        z=self.z/n
        print("除法运算=（{},{},{}）".format(x, y, z))

operation1=Operation(111,222,333)
operation2=Operation(444,555,666)
operation1.add(operation2)
operation1.sub(operation2)
operation1.mul(10)
operation1.truediv(10)

    