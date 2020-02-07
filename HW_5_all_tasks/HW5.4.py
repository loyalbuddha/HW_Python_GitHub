''' Задача 5.4. Условие:
    Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно
    данные. При этом английские числительные должны заменяться на русские. Новый блок строк
    должен записываться в новый текстовый файл.
'''

'''
    Сделаем приближённо к реальности. Пусть будет словарь перевода.
'''
num_rus_eng = {'1':['Один', 'One'],'2':['Два', 'Two'],'3':['Три', 'Three'],'4':['Четыре', 'Four']}

with open('nums_eng.txt', 'r') as nums_eng:
    content = nums_eng.readlines()
    content = [content[i].split() for i in range(0, len(content))]
    print(content)
    for el in content:
        el[0] = num_rus_eng.get(el[2])[0]
    print(content)

with open('nums_rus.txt', 'w') as nums_rus:
        for el in content:
            print(f'{el[0]} — {el[2]}')
            ''' НИЖЕ ХАРДКОД С СИМВОЛОМ "—", надо с ним разобраться '''
            nums_rus.writelines(f'{el[0]} — {el[2]}\n')
            # print(chr(8212))