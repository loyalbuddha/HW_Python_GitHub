#Запросите у пользователя значение выручки и издержек фирмы
#Определите, с каким финансовым результатом работает фирма
#(прибыль - выручка больше издержек, или убыток - издержки больше выручки).
#Выведите соответствующее соообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки
#(соотношение прибыли к выручке)
#Далее Запросите численность сотрудников фирмы
#и определите приыль фирмы в расчёте на одного сотрудника.

gain_int = int(input('Введите значение выручки, RUR: '))
charge_int = int(input('Введите значение издержек, RUR: '))
delta_int = gain_int - charge_int

if delta_int > 0:
    delta_str = str(delta_int) + ' RUR'
    print('Прибыль:', delta_str)
    profit_fl = '{:.1f}'.format(delta_int / gain_int)
    print('Рентабельность:', profit_fl)
    num_int = int(input('Введите численность персонала, шт: '))
    delta_num_fl = "{:.1f}".format(delta_int / num_int)
    print(delta_num_fl)
    delta_num_str = str(delta_num_fl) + ' RUR'
    print('Прибыль а расчёте на 1 сотрудника, RUR: ', delta_num_str)
elif delta_int < 0:
    delta_str = str(delta_int*(-1))+ ' RUR'
    print('Убыток:', delta_str)
else:
    print('Нет прибыли, зато и убыли нет')

    