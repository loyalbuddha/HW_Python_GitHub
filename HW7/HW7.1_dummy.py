def input_int(num_name = 'NoName'):
    while True:
        try:
            num = int(input(f'Enter {num_name}:\n'))
            break
        except ValueError:
            print('Нет, дай int')
    return num

#print(input_int('1'))

def matrix_size():
    print('Enter matrix size.')
    hight = input_int('hight')
    length = input_int('length')
    return hight, length

def strw():
    

print(matrix_size())