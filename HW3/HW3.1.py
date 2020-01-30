# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

#----------------------------------------- Functions ----------------------------------------
def enter_el_type():
    ''' Проверяет, что элемент имеет нужный тип и если нет, то заставляет ввести именно так'''
    while True:
            el_type = input('Какого типа будет число? float, int или complex?: ')
            if el_type == 'float' or el_type == 'int' or el_type == 'complex':
                break
            elif el_type != ('float' or 'int' or 'complex'):
                print('Нет. Ты что-то не то ввёл.')
    while True:
        try:
            element = input('Введите число: ')
            if el_type == 'complex':
                return complex(element)
                break
            elif el_type == 'int':
                return int(element)
                break
            elif el_type == 'float':
                return float(element)
                break
        except ValueError:
            print('Не-не-не-не-не, нужно число, чи с ло. Давай, попробуй ещё раз.')

def func_div(divnd,divdr):
    ''' Считает результат деления одного числа на другое, где числа (int,float,complex)'''
    if abs(divdr) != 0:
        return divnd/divdr
    else:
        print('ОПАСНОСТЬ! ОПАСНОСТЬ! ДЕЛЕНИЕ НА НОЛЬ!')
        return None

#----------------------------------------- Code ----------------------------------------

divnd = enter_el_type()
divdr =  enter_el_type()
print(f'Результат деления {divnd} на {divdr} такой: {func_div(divnd,divdr)}')