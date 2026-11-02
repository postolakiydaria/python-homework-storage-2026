#!/usr/bin/env python3


class Transport:
    """
    Базовый класс для описания общих характеристик транспорта.
    """
    def __init__(self, speed, capacity):
        self._speed = speed
        self._capacity = capacity

    @property
    def speed(self):
        """
        Возвращает скорость транспорта.
        :return: Скорость.
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        """
        Устанавливает скорость транспорта с валидацией.
        :param value: Новая скорость.
        :raises ValueError: Если скорость отрицательная.
        """
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной!")
        self._speed = value

    @property
    def capacity(self):
        """
        Возвращает вместимость транспорта.
        :return: Вместимость.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """
        Устанавливает вместимость с валидацией.
        :param value: Новая вместимость.
        :raises ValueError: Если вместимость отрицательная.
        """
        if value < 0:
            raise ValueError("Вместимость не может быть отрицательной!")
        self._capacity = value

    def __str__(self):
        """
        Возвращает строку с основными характеристиками.
        :return: Строка характеристик.
        """
        return f"{self.__class__.__name__}: Скорость {self.speed} км/ч, Вместимость {self.capacity} чел."

    def is_faster_than(self, limit):
        """
        Проверяет, превышает ли скорость заданную отметку.
        :param limit: Пороговая скорость.
        :return: True, если скорость больше.
        """
        return self.speed > limit

    @classmethod
    def from_dict(cls, data):
        """
        Создает объект из словаря с валидацией.
        :param data: Словарь с ключами speed и capacity.
        :return: Новый объект.
        :raises ValueError: Если данные некорректны.
        """
        speed = data.get("speed", 0)
        capacity = data.get("capacity", 0)
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError("Некорректная скорость в словаре: должна быть неотрицательным числом")
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Некорректная вместимость в словаре: должна быть целым неотрицательным числом")
        return cls(speed=speed, capacity=capacity)

    @staticmethod
    def get_vehicle_type():
        """
        Статический метод: возвращает тип транспорта.
        :return: Строка "Транспорт".
        """
        return "Это просто транспорт"

class Bus(Transport):
    """
    Класс автобуса. Наследуется от Transport.
    """
    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
        self._route = route

    @property
    def route(self):
        """
        Возвращает маршрут автобуса.
        :return: Маршрут.
        """
        return self._route

    @route.setter
    def route(self, value):
        """
        Устанавливает маршрут.
        :param value: Новый маршрут.
        """
        self._route = value

    def __str__(self):
        """
        Переопределяет метод родителя, добавляя маршрут.
        :return: Строка характеристик.
        """
        return super().__str__() + f" Маршрут: {self._route}"

class Truck(Transport):
    """
    Класс грузовика. Наследуется от Transport.
    """
    def __init__(self, speed, capacity, load_capacity):
        super().__init__(speed, capacity)
        self._load_capacity = load_capacity

    @property
    def load_capacity(self):
        """
        Возвращает грузоподъемность.
        :return: Грузоподъемность.
        """
        return self._load_capacity

    def calculate_delivery_cost(self, distance, price_per_km):
        """
        Считает стоимость перевозки.
        :param distance: Расстояние.
        :param price_per_km: Цена за км.
        :return: Стоимость.
        """
        return distance * price_per_km * self._load_capacity

    def __str__(self):
        """
        Переопределяет метод родителя.
        :return: Строка характеристик.
        """
        return super().__str__() + f" Грузоподъемность: {self._load_capacity} т."

    @classmethod
    def from_dict(cls, data):
        """
        Создает грузовик из словаря.
        :param data: Словарь с ключами speed, capacity и load_capacity.
        :return: Новый объект Truck.
        :raises ValueError: Если данные некорректны.
        """
        speed = data.get("speed", 0)
        capacity = data.get("capacity", 0)
        load_capacity = data.get("load_capacity", 0.0)
        if not isinstance(speed, (int, float)) or speed < 0:
            raise ValueError("Некорректная скорость в словаре")
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Некорректная вместимость в словаре")
        if not isinstance(load_capacity, (int, float)) or load_capacity < 0:
            raise ValueError("Некорректная грузоподъемность в словаре")
        return cls(speed=speed, capacity=capacity, load_capacity=load_capacity)

class Taxi(Transport):
    """
    Класс такси. Наследуется от Transport.
    """
    def __init__(self, speed, capacity, tariff):
        super().__init__(speed, capacity)
        self._tariff = tariff

    @property
    def tariff(self):
        """
        Возвращает тариф.
        :return: Тариф.
        """
        return self._tariff

    def calculate_trip_cost(self, distance):
        """
        Считает стоимость поездки.
        :param distance: Расстояние.
        :return: Стоимость.
        """
        return distance * self._tariff

    def __str__(self):
        """
        Переопределяет метод родителя.
        :return: Строка характеристик.
        """
        return super().__str__() + f" Тариф: {self._tariff} руб/км"

if __name__ == '__main__':
    bus = Bus(speed=60, capacity=30, route="ул. Ленина - ул. Мира") # создание через конструктор
    print(bus)

    truck_data = {"speed": 80, "capacity": 2, "load_capacity": 10.0} # создание через метод from_dict
    try:
        truck = Truck.from_dict(truck_data)
        print(truck)
    except ValueError as e:
        print(f"Ошибка при создании грузовика: {e}")

    print("\nПроверка валидации:") # недопустимая скорость
    try:
        bus.speed = -50
    except ValueError as e:
        print(f"Поймали ошибку: {e}")

    print(f"\nСтатический метод: {Transport.get_vehicle_type()}") # вызов статического метода без создания объекта

    print("\nПолиморфный вызов методов:")
    taxi = Taxi(speed=100, capacity=4, tariff=50.0)
    vehicles = (bus, truck, taxi)
    for vehicle in vehicles:
        print(vehicle)
