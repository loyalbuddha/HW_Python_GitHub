'''
    Реализуйте базовый класс Car . У данного класса должны быть следующие атрибуты: speed ,
    color , name , is_police (булево). А также методы: go , stop , turn(direction) , которые должны
    сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
    дочерних классов: TownCar , SportCar , WorkCar , PoliceCar . Добавьте в базовый класс метод
    show_speed , который должен показывать текущую скорость автомобиля. Для классов
    TownCar и WorkCar переопределите метод show_speed . При значении скорости свыше 60
    ( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
    атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, spd = 0, clr = 'white', nm = 'NoName', is_police = False):
        self.speed = spd
        self.color = clr
        self.name = nm
        self.is_police = is_police
        
    def go(self):
        if self.speed >= 0:
            print(f'Машина цвета {self.color} и марки {self.name} совершает Движение')
        
    def stop(self):
        print(f'Остановка')
            
    def turn(self, direction):
        print(f'Поворот: {direction}')
        
    def show_speed(self, speed):
        print(f'Скорость0: {self.speed}')
            
class TownCar(Car):
#    def __init__(self, spd = 1, clr = 'white1', nm = 'NoName1', is_police = False):
#        super().__init__(spd, clr, nm, is_police)
    
    def show_speed(self):
        if self.speed >= 60:
            print(f'Оу оу, помедленней, ты гонишь {self.speed}')
        else:
            super().show_speed(speed)
    
class SportCar(Car):
    def __init__(self, spd = 2, clr = 'white2', nm = 'NoName2', is_police = False):
        super().__init__()# clr, nm, is_police)

class WorkCar(Car):
    def __init__(self, spd = 3, clr = 'white3', nm = 'NoName3', is_police = False):
        super().__init__()# clr, nm, is_police)
        
    def show_speed(self):
        if self.speed >= 60:
            print(f'Оу оу, помедленней, ты гонишь {self.speed}')
        else:
            super().show_speed(speed)

class PoliceCar(Car):
    def __init__(self, spd = 4, clr = 'white4', nm = 'NoName4', is_police = True):
        super().__init__()# clr, nm, is_police)

car = Car()
car.go()

t_car = TownCar(61)
t_car.show_speed()
print(t_car.speed)

s_car = SportCar()

w_car = WorkCar()
p_car = PoliceCar()


