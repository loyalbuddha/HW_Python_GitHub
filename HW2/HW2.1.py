'''
    Создать список
    и заполнить его элементами различных типов данных.
    Реализовать скрипт проверки типа данных
    каждого элемента.
    Использовать функцию type()
    для проверки типа.
    Элементы списка можно не запрашивать
    у пользователя, а указать явно,
    в программе.
 '''

#создаю список
my_list = []

#заполняю список явно, в программе
my_list.append('ололо')
my_list.append(17)
my_list.append(13.2)
my_list.append(complex(12,12))
my_list.append(my_list)

''' Реализация через список '''
#ставлю в соответствие элементу списка элемент списка "тип данных"
my_list_type = []
print('Реализация через список: ')
for i in range(len(my_list)):
    my_list_type.append(type(my_list[i]))
    print(f'{my_list[i]} имеет тип данных {my_list_type[i]}')
print('\n')
    
''' И через словарь '''
my_dict = {}
for i in range(len(my_list)):
    my_dict[type(my_list[i])] = my_list[i]
    # здесь я почему-то от my_dict[my_list[i]] = type(my_list[i]) словил ошибку
print(f'Реализация через словарь: \n {my_dict}')