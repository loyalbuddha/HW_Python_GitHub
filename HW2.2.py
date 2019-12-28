#Для списка
#реализовать обмен значений соседних элементов,
#т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
#заполнение списка элементов
my_list_len = int(input('Введите длину списка: '))
while len(my_list) < my_list_len:
    my_list_el = input('Введите элемент списка: ')
    my_list.append(my_list_el)
print(my_list)

#обмен элементами вариант 1: создаём новый лист 
my_list_rev = []
i = 0
if my_list_len % 2 != 0:
    while i < my_list_len-1:
        my_list_rev.append(my_list[i+1])
        my_list_rev.append(my_list[i])
        #print(i)
        #print(my_list_rev)
        i += 2
    my_list_rev.append(my_list[my_list_len-1])

else:
    while i < my_list_len:
        my_list_rev.append(my_list[i+1])
        my_list_rev.append(my_list[i])
        #print(i)
        #print(my_list_rev)
        i += 2
print('Результат реализации варианта 1: ', my_list_rev)


#обмен элементами вариант 2: сделаем это элегантнее
my_list_rev = []
i = 0
while i < my_list_len:
    if my_list_len % 2 != 0 and i == my_list_len - 1:
        my_list_rev.append(my_list[i])
        break
    my_list_rev.append(my_list[i+1])
    my_list_rev.append(my_list[i])
    #print(i)
    #print(my_list_rev)
    i += 2
print('Результат реализации варианта 2', my_list_rev)

#обмен элементами вариант 3: через реверс через срез