'''
    Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
    сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
    типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
    параметры: размер ( для пальто) и рост ( для костюма) . Это могут быть обычные числа: V и
    H , соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
    (V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
    знания: реализовать абстрактные классы для основных классов проекта, проверить на
    практике работу декоратора @property .
'''

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name = 'NoName'):
        self.name = name
        
        @abstractmethod # то, что необходимо определить в детках класса
        def fabric_consumption(self):
            pass
    
class Coat(Clothes):
    def __init__(self, name = 'CoatNoName', size = 0):
        self.size = size
        super().__init__(name)
        
        
    def fabric_consumption(self):
        return round(self.size/6.5 + 0.5, 2) 
        
class Suit(Clothes):
    def __init__(self, name = 'SuitNoName', height = 0):
        super().__init__(name)
        self.height = height
        
    def fabric_consumption(self):
        return round(self.height*2 + 0.3) 
        
cl = Clothes()
coat = Coat()
suit = Suit()
print(cl.name)
print(coat.name)
print(suit.name)
a = coat.fabric_consumption()

while True:
    try:
        summ = 0
        cl_dict = {}
        cl_coat_u = int(input('Введите, сколько пальто вы хотите сшить: '))
        for i in range(1, cl_coat_u + 1):
            cl_coat_s = int(input(f'Введите, размер пальто номер {i}: '))
            coat = Coat(name = f'Пальто номер {i}', size = cl_coat_s)
            a = coat.fabric_consumption()
            # на всякий случай собираем словарь коллекции одежды, чтобы можно было вспомнить, что вообще мы тут напланировали
            cl_dict[f'Coat number {i}'] = ['Coat', cl_coat_s] 
            summ += a
        cl_suit_u = int(input('Введите, сколько костюмов вы хотите сшить: '))
        for i in range(1, cl_suit_u + 1):
            cl_suit_s = int(input(f'Введите, рост для костюма номер {i}: '))
            suit = Suit(name = f'Костюм номер {i}', height = cl_suit_s)
            a = suit.fabric_consumption()
            cl_dict[f'Suit number {i}'] = ['Suit', cl_coat_s]
            summ += a
        break
    except ValueError:
        print('Нет, введите int')
print(f'Суммарно надо затратить вот столько ткани, метры квадратные: {round(summ, 2)}')

print(cl_dict)