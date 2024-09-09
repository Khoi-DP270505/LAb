class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age  = age
        self.salary = salary
    def show(self):
        print(self.name, self.age, self.salary)
ema = Employee("Ema",23,7500)
ema.show()

kelly = Employee("Kelly",43,8500)
kelly.show()

