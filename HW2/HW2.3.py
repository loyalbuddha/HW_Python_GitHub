'''
    Пользователь вводит месяц в виде целого числа от 1 до 12.
    Сообщить к какому времени года относится месяц
    (зима, весна, лето, осень).
    Напишите решения через list и через dict.
'''

''' Ввод значения, такого, что это число и что оно внутри (1,12) '''
month_int = input('Введите номер месяца от 1 до 12: ')
#try:
#    month_int = int(month_int)
#except ValueError:
#    print('Нет, введите именно число!')

while True:
    num_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    if num_list.count(month_int) == 0:
        month_int = input('Нет. Введи мне номер месяца от 1 до 12: ')
        try:
            month_int = int(month_int)
        except ValueError:
            print('Нет. Введи именно число!')
    elif num_list.count(month_int) != 0:
        break

#простая реализация через list
season_list = ['winter','winter','spring','spring','spring','summer','summer','summer','autumn','autumn','autumn','winter']
print('Реализация через list. Месяц номер', month_int, 'относится к времени года', season_list[month_int-1])

#простая реализация через dict
season_dict = {1:'winter',2:'winter',3:'spring',4:'spring',5:'spring',6:'summer',7:'summer',8:'summer',9:'autumn',10:'autumn',11:'autumn',12:'winter'}
print(f'Реализация через dict. Месяц номер {month_int} относится к времени года {season_dict[month_int]}')
