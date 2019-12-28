#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц
#(зима, весна, лето, осень).
#Напишите решения через list и через dict.

month_int = int(input('Введите номер месяца от 1 до 12: '))

#простая реализация через list
season_list = ['winter','winter','spring','spring','spring','summer','summer','summer','autumn','autumn','autumn','winter']
print('Реализация через list. Месяц номер', month_int, 'относится к времени года', season_list[month_int-1])

#простая реализация через dict
season_dict = {1:'winter',2:'winter',3:'spring',4:'spring',5:'spring',6:'summer',7:'summer',8:'summer',9:'autumn',10:'autumn',11:'autumn',12:'winter'}
print('Реализация через dict. Месяц номер', month_int, 'относится к времени года', season_dict[month_int])
#.get(month_int))         