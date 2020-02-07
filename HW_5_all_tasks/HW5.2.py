'''
    Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
    подсчет количества строк, количества слов в каждой строке.
'''

'''
Файл: text.txt
Наполнение:
Generate a text file (not programmatically), save several lines in it, count 
the number of lines, the number of words in each line.
'''

with open('text.txt', 'r') as text:
    content = text.readlines()
    print(f'В файле {len(content)} строк/и')
    words_strings_num = [print(f'В строке номер {content.index(el)} находится {len(list(el.split()))} слов') for el in content]