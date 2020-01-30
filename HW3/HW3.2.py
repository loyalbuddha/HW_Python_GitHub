# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# решим задачу в 2 видах. в следовании условию задачи, задача-минимум,
# и в варианте с дофантазированием, задача-максимум

# задача-минимум: просто функция с параметрами и print'ом

# задача-максимум: пофантазируем и сделаем модификацию ДЗ 2.6 про товары
# пусть автоматически вводится номер пользователя, затем inputom заполняются его характеристики
# затем, они складываются в структуру
# затем вводится номер пользователя или какая-то его характеристика
# программа находит этого пользователя и выдаёт о нём всю информацию
# если находит несколько таких пользователей, то даёт выбор, о какой пользователе вывести информацию

#----------------------------------------- Functions ----------------------------------------

def user_char_func (user_id, name, surname, year_of_birthday, city_of_residence, email, telephone_number):
    ''' получает на вход характеристики пользователей и принтует их'''
    print(f'user id: {user_id} \n'
          f'name: {name} \n'
          f'surname: {surname} \n'
          f'year of birthday: {year_of_birthday} \n'
          f'city of residence: {city_of_residence} \n'
          f'email: {email} \n'
          f'telephone_number: {telephone_number}')


def user_char_fom_func(num_prod):
    '''
        Собирает структуру данных о пользователях
        num_prod -- число юзеров, по которым надо ввести информацию    
    '''
    for_tuple_dummy_list = []
    structure_list = []
    for_structure_dummy_tuple = ()
    dummy_dict = {'name':'','surname':'','year_of_birthday':'','city_of_residence':'','email':'','telephone_number':''}
    i = 1
    while i <= num_prod:
        for_tuple_dummy_list.append(i) 
        print(f'\nВвод данных по юзеру с id = {i} :')
        name = str(input('1. Введите name: '))
        surname = str(input('2. Введите surname: '))
        year_of_birthday = str(input('3. Введите year of birthday: '))
        city_of_residence = str(input('4. Введите city of residence: '))
        email = str(input('5. Введите email: '))
        telephone_number = str(input('6. Введите telephone_number: '))
        dummy_dict = {'name':name,'surname':surname,'year_of_birthday':year_of_birthday,'city_of_residence':city_of_residence,'email':email,'telephone_number':telephone_number}
        for_tuple_dummy_list.append(dummy_dict)
        for_structure_dummy_tuple = tuple(for_tuple_dummy_list) 
        structure_list.append(for_structure_dummy_tuple)
        for_tuple_dummy_list = []
        i += 1
    return structure_list


#----------------------------------------- Code ----------------------------------------

print(f'{user_char_func(user_id=1,surname=2,name=3,city_of_residence=4,email=5,telephone_number=6,year_of_birthday=7)} \n')
# Это к задаче-минимум

num_users = int(input('По скольким пользователям вы хотите ввести информацию: '))
print(user_char_fom_func(num_users))

user_f_char = str(input('Чтобы найти все данные про юзера, введите хоть что-то (одно), что вы знаете о искомом юзере (имя, фамилия, год рождения, город проживания, email, телефон): '))
