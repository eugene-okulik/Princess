import datetime


data = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(data, "%b %d, %Y - %H:%M:%S")
print(python_date.strftime("%B"))

human_format = datetime.datetime.strftime(python_date, "%d.%m.%Y, %H:%M")
print(human_format)
