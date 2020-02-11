'''
    Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
    (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
    три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
    реализовать переопределение метода draw . Для каждого из классов метод должен выводить
    уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
    метод для каждого экземпляра.
'''
    
class Stationery:
    def __init__(self, title = 'none'):
        self.title = title
        
    def draw(self):
        print('Запуск отрисовки')
        
class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')
    
class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')
        
class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')
        
st = Stationery()
pen = Pen('1')
pencil = Pencil(2)
handle = Handle(3)

print(f'Stationery: {st.title}, Pen: {pen.title}, Pencil: {pencil.title}, Handle: {handle.title}')
print(f'Stationery: {st.draw()}, Pen: {pen.draw()}, Pencil: {pencil.draw()}, Handle: {handle.draw()}')
