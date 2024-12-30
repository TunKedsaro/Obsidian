class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age  = age
        self.salr = salary
    def detail(self):
        print("Name:",self.name)
        print("Age :",self.age)
        print("salr:",self.salr)