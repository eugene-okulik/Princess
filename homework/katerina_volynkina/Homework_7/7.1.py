while True:
    result_input = int(input('Назови цифру: '))
    result = 8
    if result_input == result:
        print("Поздравляю! Вы угадали!")
        break
    if result_input != result:
        print("Попробуйте снова")
