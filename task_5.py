"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(self.title, 'рисует.')


class Pencil(Stationery):
    def draw(self):
        print(self.title, 'рисует.')


class Handle(Stationery):
    def draw(self):
        print(self.title, 'рисует.')


stationery = Stationery('printer')
stationery.draw()
stationery_2 = Pen('Ручка')
stationery_2.draw()
stationery_3 = Pencil('Карандаш')
stationery_3.draw()
stationery_4 = Handle('Маркер')
stationery_4.draw()
