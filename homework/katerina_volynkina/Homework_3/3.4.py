# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь


def hypotenuse(x, y):
    return (x ** 2 + y ** 2) ** 0.5


def triangle_area(x, y):
    return (x * y) / 2


print(hypotenuse(2, 1))
print(triangle_area(2, 3))
