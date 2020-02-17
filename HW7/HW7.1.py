'''
    Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
    __init__() ), который должен принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — с истема некоторых математических величин, расположенных в виде
    прямоугольной схемы.
    Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
    
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
    привычном виде.
    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
    объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
    Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
    строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

''' я хочу, чтобы в матрице автоматом были отступы для всех элементов матрицы в случае,
    если хоть 1 элемент превышает остальные в числе знаков. Для этого я использую NumPy, чтобы
    не изобретать велосипед заново
    +
    сделаю генератор случайных чисел для матрицы
'''


from random import randint
import numpy 


class Matrix:
    def __init__(self, hight = 3, length = 3, my_list = [[0]]):
        self.hight = hight
        self.length = length
        self.my_list = [[0 for el in range(0, self.length)] for le in range(0, self.hight)]
    
    def input_int(self, num_name = 'NoName'):
        ''' ввод интовых чисел - это для def matrix_size'''
        while True:
            try:
                num = int(input(f'Enter {num_name}:\n'))
                break
            except ValueError:
                print('Нет, дай int')
        return num
    
    def matrix_size(self):
        ''' определение размера матрицы '''
        print('Enter matrix size.')
        self.hight = self.input_int(num_name = 'hight')
        self.length = self.input_int(num_name = 'length')
        return self.hight, self.length
    
    def __str__(self):
        print(f'{numpy.array(self.my_list)}')
       
    def rand_matrix(self):
        ''' заполнение матрицы заданного размера рандумными числами от 90 до 110 '''
        self.my_list = [[randint(90, 110) for el in range(0, self.length)] for le in range(0, self.hight)]
        self.matrix = numpy.array(self.my_list)
        return self.matrix
        
    def __add__(self, other):
        ''' сложение матриц размера i на j '''
        a = len(self.my_list) != len(other.my_list)
        b = len(self.my_list[0]) != len(other.my_list[0])
        if a or b:
            return print('Размеры матриц не совпадают, Алярм!')
        summ = self.my_list
        for i in range(0, len(self.my_list)):
            for j in range(0, len(other.my_list[0])):
                summ[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return numpy.array(summ)
        
m = Matrix(hight = 4, length = 5)
n = Matrix(hight = 4, length = 5)
m.rand_matrix()
n.rand_matrix()
#print('\n')
#m.__str__()
#print('\n')
#print(m.my_list)
print(f'{m + n}')


 
# print(f'{m.my_list}')
# print(m.matrix_size())
#m.__str__()
#print(f'{m.hight}, {m.length}')

#m.rand_matrix()
#m.__str__()

#print(m.matrix)

#m.__add__()

''' это было очень классное задание, спасибо! '''