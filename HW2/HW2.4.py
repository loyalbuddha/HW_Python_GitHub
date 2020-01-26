'''
    Пользователь вводит строку из нескольких слов, разделённых пробелами.
    Вывести каждое слово с новой строки.
    Строки необходимо пронумеровать.
    Если в слово длинное, выводить только первые 10 букв в слове.
'''

my_words_str0 = str(input('Введите строку из нескольких слов: '))

''' Вариант решения 1. "я люблю всё усложнять" '''

my_words_str = my_words_str0
#my_words_str = ('строка12345678 из12345678910 нескольких1234567890 слов1234567890 это строка из нескольких слов')

#подготовительные работы
my_words_list = list(my_words_str) #перевод строки в список
my_words_list.insert(0,' ') #добавляем в начало пробел
my_words_list.append(' ') #добавляем в конец пробел
my_words_num_int = my_words_list.count(' ') #сколько пробелов

#разобъём действо на 3 функции и будем решать их отдельно

#сперва сократим длину слов, превышающих 10 букв
#для этого возмём расстояние между пробелами
#и если оно больше 10, то удалим "лишние" элементы
dummy = 0
i = 0
k = 0
delta2 = 0
while i < len(my_words_list):
    if my_words_list[i] == ' ': #проверка на >10 симоволов в слове
        delta = i - dummy - 1
        dummy = i
        if delta > 10: #сокращение слова
            delta2 = delta - 10
            k = i
            while delta2 > 0: #удаление сиволов от i-символа на delta2 символов назад
                delta2 -= 1
                k -= 1
                my_words_list.pop(k)
                dummy = k
    i += 1

#выводим слова с новой строки и одновременно нумеруем перенос
i = 0
n = 0
while n <= my_words_num_int:
    while  i < len(my_words_list):
        if my_words_list[i] == ' ' and i != len(my_words_list)-1:
            my_words_list.pop(i)
            #закидываем в один элемент перенос строки и её номер
            #пользуясь тем, что при переводе в str они будут почитаты 
            my_words_list.insert(i,'\n'+str(n)+' ')
            break
        i += 1
    n += 1
    
#пользователю я буду выводить строку
my_words_str = str(my_words_list)

#так как я не нашёл, как преобразовать список в строку, то
#делаю цикл для собирания строки из списка поэлементно
my_words_str = ''
i = 0
while i < len(my_words_list):
    my_words_str =  my_words_str + my_words_list[i]
    i += 1
    
#Конечный результат:
print(my_words_str)

'''
    Вариант 2. После покуривания мануала. Использованы фичи:
    .split()        рубит по символу пробела строку в список из порубленных элементов;
    for i in        цикл с записью короче чем while;   
    range()         итерируемый список от 0 до того, что внутри скобок, чтобы быстрее записать ;
    Срез [:10]      удобная фича, чтобы избавиться от лишних элементов;
'''
my_words_list = my_words_str0.split()
for i in range(len(my_words_list)):
    print(i,my_words_list[i][:10]) #возможно, отсутствие if- проверки на >10 символов как-то утяжелит производительность

'''
    Вариант 3. После покуривания мануала. Использованы фичи:
    for i, el in enumerate()    позволяет пробегать по нумерованному поэлементно списку                 
'''
for i, el in enumerate(my_words_list):
    print(i, el[:10]) #возможно, отсутствие if- проверки на >10 символов как-то утяжелит производительность