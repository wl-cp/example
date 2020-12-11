class Employee(object):
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def display(self):
        print(f"姓名:{self.name} 编号:{self.number}")
        
class Sales(Employee):
    def __init__(self,name,number,xiaoshoue):
        super().__init__(name, number)
        self.xiaoshoue = xiaoshoue
        self.gongzi = 0.1 * self.xiaoshoue
    def display(self): 
        print(f"销售员   姓名:{self.name} 编号:{self.number} 工资:{self.gongzi}")
class Manager(object):
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.gongzi = 8000
    def display(self):
        print(f"  经理   姓名:{self.name} 编号:{self.number}  工资:{self.gongzi}")
class SalesManager(Sales,Manager):
    def __init__(self,name,number,xiaoshoue):
        super().__init__(name,number,xiaoshoue)
        self.gongzi = 5000 + 0.05 * self.xiaoshoue
    def display(self):
        print(f"销售经理 姓名:{self.name} 编号:{self.number}   工资:{self.gongzi}")   
s = Sales('mao',110,10000)
s.display()
m = Manager('mao',11)
m.display()
sm = SalesManager('mao',1,10000)
sm.display()
        
        
        
        