'''
    Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
    surname , position (должность), income (доход). Последний атрибут должен быть
    защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
    {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
    В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
    дохода с учетом премии ( get_total_income ). Проверить работу примера на реальных данных
    (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
    вызвать методы экземпляров).
'''

class Worker:
#базовый класс
    def __init__(self, n = 'NoName', sn = 'NoSurname', wg = 0, bns = 0):
        self.name = n
        self.surname = sn
        self.wage = wg
        self.bonus = bns
        self._income = {'wage': self.wage, 'bonus': self.bonus}    
    
    
class Position(Worker):
# наследующий класс
    def __init__(self, n = 'NoName2', sn = 'NoSurname2', wg = -1, bns = -1, ps = 'NoPosition'):
        super().__init__(n, sn, wg, bns)
        self.position = ps
        
    
    def get_full_name(self):
        return print(f'Полное ФИО: {self.name} {self.surname}')
        
    def get_total_income(self):
        #summa = 0 
        #for el in self._income:
        #    summa += self._income.get(el) сделаю через sum({}.values())
        return print(f'оклад {self._income.get("wage")} + премия {self._income.get("bonus")} = {sum(self._income.values())}')
    
w = Worker('a', 'b', 10, 11)
print(f'Worker \nname: {w.name} \nsurname: {w.surname} \nwage: {w.wage} \nbonus: {w.bonus}')
print(w._income)

p = Position('Эрлих', 'Эрлихович', 12, 13, 'Woorker')
print(f'Position\nname: {p.name} \nsurname: {p.surname} \nwage: {p.wage} \nbonus: {p.bonus}'
      f'\nposition: {p.position}')

p.get_full_name()
print(p._income)
p.get_total_income()

