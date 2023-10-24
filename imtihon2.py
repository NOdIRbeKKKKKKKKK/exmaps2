class Worker:
    def __init__(self,Familiya,Lavozimi,salary) -> None:
        self.Surname=Familiya
        self.Position=Lavozimi
        self.salary=salary
    def pulini_oshir(self,ishchi):
        for i in range(ishchi):
            a=self.Surname*15//100

son=int(input("NEchta ishchi qoshmoqchisiz: "))
lst=[]
for i in range(son):
    obj=Worker(input("Ismni kiriting: "),input("Lavozimni kiriting: "),int(input("oyligni kiriting: ")))
    lst.append(obj)

for i in lst:
    i.pulini_oshir(son)    


# 100//0.15
