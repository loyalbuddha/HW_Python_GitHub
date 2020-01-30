# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов

# Я сделал в 2 вариантах. В варианте минимум. Аргументы - целые числа. 
# И в варианте Сделаем круче: пусть функция принимает сколько угодно аргументов
# и возвращает сумму наибольших 2, максимум, медиану и среднее

#----------------------------------------- Functions ----------------------------------------

def my_func(arg1, arg2, arg3):
    ''' Функция, возвращающая сумму двух наибольших аргументов из трёх введённых '''
    args_list = [arg1,arg2,arg3]
    args_list.remove(min(args_list))
    return min(args_list) + max(args_list)

def my_func_more(*args):
    ''' Функция, возвращающая сумму двух наибольших аргументов, медиану и среднее. Из многих '''
    args_list = [*args]
    first_max_args = max(args_list)
    medn = sorted(args_list)[len(args_list)//2]
    if len(args_list) % 2 != 0:
        medn = sorted(args_list)[len(args_list)//2]
    elif len(args_list) % 2 == 0:
        medn = (sorted(args_list)[len(args_list)//2] + sorted(args_list)[1+(len(args_list)//2)])/2
    summ = 0
    for el in args_list:
        summ += el
    args_list.remove(first_max_args)
    return first_max_args + max(args_list), medn, summ/len(args_list)

#----------------------------------------- Code ----------------------------------------

print(my_func(20,9,0))
print(my_func_more(5,17,20,30,1000))
