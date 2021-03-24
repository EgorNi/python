"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""
import random

class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'is going')

    def stop(self):
        print(self.name, 'stopped')

    def turn(self, direction):
        print(self.name, 'turned', direction)

    def show_speed(self):
        print(self.name, 'speed is: ', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('slow down your speed')
        else:
            print(self.name, 'speed is: ', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('slow down your speed')
        else:
            print(self.name, 'speed is: ', self.speed)


class PoliceCar(Car):
    pass


current_speed = round(random.random() * 100)
car = Car(current_speed, 'dark blue', 'Suzuki', False)
work_car = WorkCar(current_speed, 'green', 'AUDI', False)
town_car = TownCar(current_speed, 'black', 'FAW', False)
sport_car = SportCar(current_speed, 'white', 'Aston Martin', False)
police_car = PoliceCar(current_speed, 'blue', 'LADA', True)
work_car.go()
town_car.show_speed()
sport_car.show_speed()
car.turn('right')
police_car.stop()
