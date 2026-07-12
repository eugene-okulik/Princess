def calculate(func):
    def wrapper(first, second):
       if first < 0 or second < 0:
           return first * second
       elif first > second:
           return first - second
       elif first < second:
           return first / second
       elif first == second:
           return first + second
    return wrapper

@calculate
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    else:
        return first / second


a = int(input('Введите первое число '))
b = int(input('Введите второе число '))

print(calc(a, b))