class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary(self):
        return self.salary
    
    def get_tax(self):
        return self.salary * .2
    
if __name__ == '__main__':
    employee = Employee('Misha', 'CTO', 7800)
    print(employee.get_salary())
    print(employee.get_tax())
