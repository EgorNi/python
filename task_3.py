"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'full name is: {self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income.get("wage") + (self._income.get("bonus"))


salary = {"wage": 100000, "bonus": 50000}
data_2 = Position('Leonid', 'Agutin', 'signer', salary)
print(data_2.get_full_name())
print('total income: ', data_2.get_total_income())
