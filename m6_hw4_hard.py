from math import sqrt


class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *args):
        self.__color = []
        self.set_color(*color)
        self.__sides = []
        example_sides = []
        if len(args) == self.sides_count:
            example_sides = list(args)
        elif len(args) != self.sides_count:
            for i in range(self.sides_count):
                if len(args) != 1:
                    example_sides.append(1)
                elif len(args) == 1:
                    example_sides.append(*args)
        self.set_sides(*example_sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return r in range(256) and g in range(256) and b in range(256)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *args):
        for i in args:
            if not isinstance(i, int) or i <= 0 or len(args) != self.sides_count:
                return False
        return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides.clear()
            self.__sides.extend(new_sides)

    def __len__(self):
        self.res = 0
        for i in self.__sides:
            self.res += i
        return self.res


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *args):
        super().__init__(rgb, *args)

    def __radius(self):
        return len(self) / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius() ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *args):
        super().__init__(rgb, *args)

    def __height(self):
        self.p = len(self) / 2
        return 2 * sqrt(self.p * (self.p - self.get_sides()[0]) * (self.p - self.get_sides()[1])
                    * (self.p - self.get_sides()[2])) / self.get_sides()[0]

    def get_square(self):
        return self.__height() * self.get_sides()[0] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *args):
        super().__init__(rgb, *args)

    def __sides(self, side):
        self.set_sides(side, side, side, side, side, side, side, side, side, side, side, side)

    def get_volume(self, side):
        self.__sides(side)
        return self.get_sides()[0] * self.get_sides()[0] * self.get_sides()[0]


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
trigangle1 = Triangle((155, 155, 155), 2, 3)
cube1 = Cube((222, 35, 130), 6)

#  Проверка создания фигур
print('--Circle--')
print(circle1.get_color())
print(circle1.get_sides())
print('--Trigangle--')
print(trigangle1.get_color())
print(trigangle1.get_sides())
print('--Cube--')
print(cube1.get_color())
print(cube1.get_sides())

# Проверка на изменение цветов:
print()
print('Проверка на изменение цветов:')
print('--Circle--  --должен измениться, изначально был (200, 200, 100)')
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
print('--Trigangle--  --меняться не должен, т.к. тип float, был (155, 155, 155)')
trigangle1.set_color(15.5, 55, 55)
print(trigangle1.get_color())
print('--Cube--  --меняться не должен, т.к. значение более 255, был (222, 35, 130)')
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
print()
print('Проверка на изменение сторон:')
print('--Circle--  --должен измениться, изначально был [10]')
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
print('--Trigangle--  --должен измениться, был [1, 1, 1]')
trigangle1.set_sides(5, 5, 5)
print(trigangle1.get_sides())
print('--Cube--  --меняться не должен, т.к. сторон больше чем 5, был [6, 6, 6, ... , 6]')
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

# Проверка периметра (круга), это и есть длина:
print()
print('Проверка на расчет периметра:')
print('--Circle--  --должен быть - 15')
print(len(circle1))
print('--Trigangle--  --должен быть - 15')
print(len(trigangle1))
print('--Cube--  --должен быть - 72')
print(len(cube1))

# Проверка доп функция круга:
print()
print('Проверка доп функция круга: площадь должна быть примерно = 17.914')
print(circle1.get_square())

# Проверка доп функция круга:
print()
print('Проверка доп функция треугольника: площадь должна быть примерно = 10.825')
print(trigangle1.get_square())

# Проверка доп функция куба:
print()
print('Проверка доп функция куба: объем должен быть примерно = 125')
print(cube1.get_volume(5))
