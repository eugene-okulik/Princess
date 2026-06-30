text_1 = 'результат операции: 42'
text_2 = 'результат операции: 54'
text_3 = 'результат работы программы: 209'
text_4 = 'результат: 2'

def res(text):
    result = text.split(': ')
    print(int(result[1]) + 10)

res(text_1)
res(text_2)
res(text_3)
res(text_4)