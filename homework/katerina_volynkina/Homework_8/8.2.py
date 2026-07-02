import sys

sys.set_int_max_str_digits(30000)


def generator_fibonacci(limit=100):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


data = [5, 200, 1000, 100000]
count = 1

for i in generator_fibonacci(100001):
    for j in data:
        if count == j:
            print(i)
            break
    count += 1
