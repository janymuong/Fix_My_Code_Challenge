#!/usr/bin/python3
'''module:
I love geometry! - file for a square class
'''


class Square():
    '''repr for a square class'''
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        '''constructor to initialze attributes'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        '''area of the square'''
        return self.width * self.height

    def PermiterOfMySquare(self):
        '''perimeter of a geometric square'''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''return string representation of square'''
        return '{}/{}'.format(self.width, self.height)


if __name__ == '__main__':

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
