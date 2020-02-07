'''
    Реализовать формирование списка, используя функцию range() и возможности генератора. В
    список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
    результат вычисления произведения всех элементов списка.
    Подсказка: использовать функцию reduce() .
'''

from functools import reduce

''' поэтапно, сначала реализуем список, затем результат произведения эл-тов списка '''
new_list = [el for el in range(100, 1001) if el % 2 == 0] #range(100, 1001) 
composition = reduce((lambda el1, el2: el1 * el2), new_list)

''' или оба этапа в 1 строку '''
composition = reduce((lambda el1, el2: el1 * el2), [el for el in range(100, 1001) if el % 2 == 0])

''' или вспоминая, что в range(от,до,шаг) и модифицируя избавляя себя от if '''
composition = reduce((lambda el1, el2: el1 * el2), [el for el in range(100, 1001, 2)])