'''
    Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
    значение. При вызове функции должен создаваться объект-генератор. Функция должна
    вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала
    числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
    Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
    четырёх 4! = 1 * 2 * 3 * 4 = 24.

    факториалы:
    1! = 1
    2! = 1! * 2 = 2
    3! = 2! * 3 = 6
    4! = 3! * 4 = 24
    5! = 4! * 5 = 120
    
    Далее, чтобы не потерять, я пишу все этапы своей разработки конечного варианта
'''

''' 1. сперва найдём факториал по-тупому
new_list = [el for el in range(1, 11)]
print(new_list)
factr = 1
i = 1
while i < len(new_list):
    factr = new_list[i] * factr
    i += 1
    print(factr)
    '''

''' 2. усовершенствуем с while до for 
factr = 1
for el in new_list:
    factr = el * factr
    print(factr)
    '''

''' 3. усовершенствуем до того, чтобы лист формировался без доп записи, формирующей new_list
factr = 1
for el in [le for le in range(1, 11)]:
    factr = el * factr
    print(factr)
    '''

''' 4. запишем это в виде функции возвращающей значение через yield '''
def fact(n):
    factr = 1
    for el in [le for le in range(1, n+1)]:
        factr *= el
        yield factr

for el in fact(5):
    print(el)