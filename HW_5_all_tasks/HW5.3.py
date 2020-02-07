''' Условие:
    Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
    величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
    20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
    сотрудников.
    Пример файла:
    Иванов 23543.12
    Петров 13749.32
'''


''' Пояснение:
    в моём файле структура такая:
    Иванов 23543.12 RUR
    Петров 13749.32 RUR
    Leonenko 200 DOL
    Karpov 30000 DOL
    Gendalf_White 10000000 DOL
    и происходит конвертация из DOL в RUR (я решил заморочиться, потому что хотел
    сделать генератор списка, который просто подменяет внутри списка значения, но
    диковинно сломал себе мозг и ушёл спать)
'''
file_name = str(input('Введите название файла:\n'))
min_money = float(input('Введите минимальный размер оклада:\n'))
current_rate = float(input('Введите курс доллара к рублю:\n'))

try:
    with open(file_name, 'r') as money:
        content = money.readlines()
        content = [content[i].split() for i in range(0, len(content))]
        for el in content: # вот это я хочу сделать в 1 строчку, но мне не хватает опыта
            el[1] = float(el[1])/current_rate if el[2]=='DOL' else el[1]
            el[2] = 'RUR' if el[2]=='DOL' else el[2]        
        name_min = [el[0] for el in content if float(el[1]) <= min_money]
        avg_money = sum([float(el[1]) for el in content])/len(content)
        print(f'Сотрудники, получающие меньше {min_money} рублей:\n{name_min}')
        print(f'Средняя величина дохода сотрудников:\n{avg_money:.2f} рублей')
except FileNotFoundError:
        print('Что-то с файликом не так')
    
        