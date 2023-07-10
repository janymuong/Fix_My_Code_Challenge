#!/usr/bin/python3
'''module:
I love geometry! - file for a square class
'''


class Square():
    '''repr for a square class'''
    size = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        '''area of the square'''
        return self.size ** 2

    def PermiterOfMySquare(self):
        '''perimeter of a geometric square'''
        return (self.size * 4)

    def __str__(self):
        '''return string representation of square'''
        return f'{self.size}/{self.size}'


if __name__ == '__main__':

    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
