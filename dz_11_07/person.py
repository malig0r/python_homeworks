class Person:
    def __init__(self, name: str, age: float):
        self.name = name
        self.age = age

    def say_hello(self) -> None:
        print(f'Привет, меня зовут {self.name.title()}, и мне {self.age} лет')

    def can_vote(self) -> bool:
        if self.age >= 18:
            return True
        else: 
            return False
        
if __name__ == '__main__':
    igor = Person('igor', 31)
    igor.say_hello()
    print(igor.can_vote())
    lesha = Person('lesha', 17)
    print(lesha.can_vote())

