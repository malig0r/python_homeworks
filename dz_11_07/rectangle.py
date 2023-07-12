class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width 
    
    def get_perimeter(self):
        return self.height * 2 + self.width * 2
    
    def is_square(self):
        if self.height == self.width:
            return True
        else:
            return False
        
if __name__ == '__main__':
    rectangle = Rectangle(4, 2)
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
    print(rectangle.is_square())
    square = Rectangle(2, 2)
    print(square.is_square())
