class Car:
    def __init__(self, make: str, model: str, year: int, speed: float):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, acceleration: float):
        self.speed += acceleration

    def brake(self, braking: float):
        self.speed -= braking

    def get_speed(self):
        return self.speed

if __name__ == "__main__":
    car = Car('bmw', 'm3', 2021, 99.9)
    car.accelerate(10.1)
    print(car.get_speed())
    car.brake(10)
    print(car.get_speed())