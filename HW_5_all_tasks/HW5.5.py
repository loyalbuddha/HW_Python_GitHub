''' Задача 5.5. Условие:
    Создать (программно) текстовый файл, записать в него программно набор чисел,
    разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
    ее на экран.
'''
from random import randint

num = int(input('Введите, сколько чисел запишется в файл:\n'))
with open('new_file.txt', 'w') as new_file:
    rand_num_list = [randint(0, 10) for el in range(0, num)]
    for el in rand_num_list:
        new_file.write(f'{str(el)} ')
    
with open('new_file.txt', 'r') as new_file:
    content = new_file.readlines()[0].split()
    summ = 0
    for el in content:
        el = int(el)
        summ += el
    print(f'Сумма чисел: {summ}')
    