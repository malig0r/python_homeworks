
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         print(f'Привет, меня зовут {self.name}, и мне {self.age} лет.')

# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#     def get_area(self):
#         return self.height * self.width 
#     def get_perimeter(self):
#         return self.height * 2 + self.width * 2
   
# class BankAccount:
#     def __init__(self, balance, interest_rate):
#         self.balance = balance
#         self.interest_rate = interest_rate

#     def deposit(self, value):
#         self.balance += value

#     def withdraw(self, value):
#         self.balance -= value    

#     def add_interest(self):
#         self.balance += self.balance / 100 * self.interest_rate

class Student():
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average_grade(self):
        return sum(self.grades)/len(self.grades)
    def is_honors_student(self):
        if self.get_average_grade() > 4.5:
            return True
        else:
            return False
        




if __name__ == "__main__":
    # rect = Rectangle(10, 5)
    # print(rect.get_area())
    # print(rect.get_perimeter())
    # account = BankAccount(0, 10)
    # account.deposit(110)
    # print(account.balance)
    # account.withdraw(10)
    # print(account.balance)
    # account.add_interest()
    # print(account.balance)
    stud = Student('Misha', 22)
    stud.add_grade(4)
    print(stud.is_honors_student())

