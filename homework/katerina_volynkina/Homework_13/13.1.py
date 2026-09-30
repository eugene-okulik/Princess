import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
princess_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(princess_path, encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


f = []
for data_line in read_file():
    data_base = data_line[3:30].strip()
    data_format = datetime.datetime.strptime(data_base, '%Y-%m-%d %H:%M:%S.%f')
    f.append(data_format)


data_1 = f[0] + datetime.timedelta(days=7)
print(data_1)
data_2 = f[1].strftime('%A')
print(data_2)
now = datetime.datetime.now()
data_3 = now - f[2]
print(data_3.days)
