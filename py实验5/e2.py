class Person(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display(self):
        print(f"姓名:{self.name} id:{self.id}")
        
class Student(Person):
    def __init__(self,id,name,cla,soure):
        super().__init__(id,name)
        self.cla = cla
        self.soure = soure
    def display(self):
        print(f"姓名:{self.name}   id:{self.id}   班级:{self.cla}    成绩:{self.soure}")
        
class Teacher(Person):
    def __init__(self, id,name,zhicheng,bumen):
        super().__init__(id, name)
        self.zhicheng = zhicheng
        self.bumen = bumen
    def display(self):
        print(f"姓名:{self.name}    id:{self.id}    职称:{self.zhicheng}    部门:{self.bumen}")

s=Student(12,'wang','一班',99)
s.display()
t=Teacher(1,'li','教授','自动化') 
t.display()      
