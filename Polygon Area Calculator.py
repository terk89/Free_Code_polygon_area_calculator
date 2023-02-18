"""
In this project you will use object oriented programming to create
a Rectangle class and a Square class. The Square class should be a
subclass of Rectangle and inherit methods and attributes.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        picture = ''
        if self.height > 50 or self.width > 50:
            return 'Too big for picture'
        for i in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        counter = 0
        if self.width < shape.width or self.height < shape.height:
            return 0
        elif self.width == shape.width and self.height == shape.height:
            return 1
        else:
            tmp_height = self.height
            while tmp_height >= shape.height:
                tmp_width = self.width
                while tmp_width >= shape.width:
                    tmp_width -= shape.width
                    counter += 1
                tmp_height -= shape.height
            return counter


class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.height = side
        self.width = side


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))