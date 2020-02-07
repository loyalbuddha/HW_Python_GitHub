'''
    Создать программно файл в текстовом формате, записать в него построчно данные,
    вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

''' В 2 вариантах, потому что я не знаю трудозатратность открытия файла или
трудозатратность удерживания файла в открытом виде.
    Итак, в первом случае файл открывается 1 раз и в него вносятся строки;
    во втором случае он открывается столько раз, сколько в него записывается.
'''

''' 1 вариант '''
with open('text.txt', 'a') as text_file: # 1 раз открываем файл
    while True:
        line = input('Enter text (1): ')
        if line == '': # if not line
            text_file.close()
            break
        else:
            print(line, file=text_file) # text_file.write(f'{line}\n')
            
''' 2 вариант '''
while True:
    line = input('Enter text (2): ')
    if line == '':      
        break
    with open('text2.txt', 'a') as text_file: # каждый раз открываем файл на внесение строки
        print(line, file = text_file)
        text_file.close()
            