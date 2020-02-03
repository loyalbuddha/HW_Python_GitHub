
def input_2_num():
    while True:
        try:
            start = int(input('Введите начальное число: '))
            while True:
                try:
                    finish = int(input('Введите конечное число: '))
                    break
                except ValueError:
                    print('Нет, это должно быть число. Попробуйте ещё')
            break
        except ValueError:
            print('Нет, это должно быть число. Попробуйте ещё')
    return start, finish

# def input_n_num()