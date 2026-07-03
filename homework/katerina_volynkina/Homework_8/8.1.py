import random


salary = int(input('Введите свою зарплату: '))
bonus = random.choice([True, False])
if bonus:
    print(f"({salary}, {bonus} -'${salary*random.randrange(1, 50)}')")
else:
    print(salary)
