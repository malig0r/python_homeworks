from functools import total_ordering

@total_ordering
class RealString:
    def __init__(self, string):
        self.string = string

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.string) < len(other.string)
        else:
            return len(self.string) < len(f'{other}')
    
    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.string) == len(other.string)
        else:
            return len(self.string) == len(f'{other}')


    
if __name__ == '__main__':
    str1 = RealString('Молоко')
    str2 = RealString('Абрикосы растут')
    str3 = 'Золото'
    str4 = [1, 2, 3]
    print(str1 < str4)
    print(str1 >= str2)
    print(str1 == str3)