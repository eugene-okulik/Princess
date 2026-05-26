# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел


def calculate_result(x, y):
    return (x + y) / 2, (x * y) ** 0.5


print(calculate_result(2, 8))
