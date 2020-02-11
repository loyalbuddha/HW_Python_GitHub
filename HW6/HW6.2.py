'''
    Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
    (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
    Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
    для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
    асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
    толщины полотна. Проверить работу метода.
    Например: 20м*5000м*25кг*5см = 12500 т
'''

class Road:
    def __init__(self, length = 0, width = 0):
        self._length = length # одно подчёркивание - это защищённый атрибут
        self._width = width 
        self.density = 0.000001 # тонн на сантиметр^3
    
    def input_l_w(self):
        ''' override _length and _width '''
        print(f'По дефолту стоят length = {self._length}m и width = {self._width}m')
        while True:
            try:
                self._length = int(input('Enter new length, metres:\n'))
                break
            except ValueError:
                print('Error. You need to enter int.')
        while True:
            try:
                self._width = int(input('Enter new width, metres:\n'))
                break
            except ValueError:
                print('Error. You need to enter int.')
        return self._length, self._width
       
    def asp_mass(self):
        mass = self._length * self._width * self.density * 10**4
        return f'{self._length}м*{self._width}м*{self.density}тонн/см^3 = {mass} тонн'

my_instance = Road()
my_instance.input_l_w()
print(my_instance._length)
print(my_instance.asp_mass())