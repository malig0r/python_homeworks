class Dog:
    def __init__(self, name: str, breed: str, age: float):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print('Гав-гав!')

    def get_human_age(self):
        if self.age <= 2:
            return self.age * 10.5
        else:
            return (self.age - 2) * 4 + 21 
        
if __name__ == '__main__':
    dog = Dog('Fuxia', 'Basenji', 1.9)
    dog.bark()
    print(f'Возраст собаки, приведенный к человеческому: {dog.get_human_age():.0f}')
