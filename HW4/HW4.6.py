'''
    Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
    создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
    завершения.
    Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
    завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
    повторение элементов списка будет прекращено.
'''

from itertools import count, cycle, islice
from random import randint
from for_HW46 import input_2_num

''' input_2_num - это следующая функция: ''' '''
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
'''

start, finish = input_2_num()
 
''' для count '''
def iter_count(start, finish):
    for i in islice(count(start), (finish - start + 1)): # хорошая замена if
            yield i

second_list = []
for el in iter_count(start, finish):
    second_list.append(el)
print(f'Целые числа, начиная с указанного {start} и заканчивая указанным {finish}:\n{second_list}\n')
    
''' для cycle '''
first_list = [randint(0, 10) for el in range(0, randint(0, 20))]

second_list = []
c = 0
for el in islice(cycle(first_list), (finish - start + 1)):
    if c > 30:
        break
    else:
        second_list.append(el) #сделал лист, чтобы проще было отслеживать чиселки - не по вертикали, а по горизонтали
    c += 1
print(f'first_list: {first_list}\nsecond_list: {second_list}')