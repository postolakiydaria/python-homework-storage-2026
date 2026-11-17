class Transport:
    """
    Базовый класс транспортного средства.
    Хранит скорость и ёмкость, проверяет их корректность при создании
    """
    def __init__(self, speed, capacity):
        """
        Создаёт транспорт с заданными скоростью и ёмкостью.

        :param speed: скорость транспорта
        :param capacity: ёмкость транспорта

        """
        if speed <= 0:
            raise ValueError("Скорость должна быть > 0")
        if capacity <= 0:
            raise ValueError("Ёмкость должна быть > 0")
        self._speed = speed
        self._capacity = capacity

    @property
    def speed(self):
        """возвращает скорость"""
        return self._speed

    @property
    def capacity(self):
        """возвращает емкость"""
        return self._capacity

    def __str__(self):
        """
        возвращает информацию о транспорте
        :return: строка вида "Скорость:..., Ёмкость:..."
        """
        return f"Скорость: {self.speed}, Ёмкость: {self.capacity}"

    def is_fast(self, limit=100):
        """
        Проверяет, превышает ли скорость транспорта заданную отметку
        :param limit: заданная отметка для сравнения (автоматически 100)
        :return: True - если превышает, иначе False
        """
        return self.speed > limit

    @classmethod
    def from_dict(cls, some_dict):
        """
        Создает объект транспорта из словаря
        :param some_dict: словарь
        :return: новый обьект класса cls
        :raises ValueError: если в словаре отсутствует ключ "speed" или "capacity"
        """
        speed = some_dict.get("speed")
        capacity = some_dict.get("capacity")
        if speed is None or capacity is None:
            raise ValueError("В словаре должны быть ключи speed и capacity")
        return cls(speed, capacity)

class Bus(Transport):
    """Автобус: транспорт с маршрутом"""
    def __init__(self, speed, capacity, route):
        """
        Создаёт автобус с заданными скоростью, ёмкостью и маршрутом
        :param speed: скорость автобуса
        :param capacity: емкость автобуса
        :param route: маршрут автобуса
        """
        super().__init__(speed, capacity)
        self.__route = route

    @property
    def route(self):
        """возвращает маршрут"""
        return self.__route

    @route.setter
    def route(self, value):
        """Устанавливает маршрут с проверкой на непустую строку"""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Надо написать маршрут текстом и маршрут не должен быть пустой строкой")
        self.__route = value

    def __str__(self):
        """возвращает информацию о автобусе, включая маршрут"""
        return super().__str__() + f", Маршрут: {self.route}"

    @classmethod
    def from_dict(cls, some_dict):
        """
        Создает объект автобуса из словаря
        :param some_dict: словарь
        :return: новый обьект класса Bus
        :raises ValueError: если в словаре отсутствует один из нужных ключей
        """
        speed = some_dict.get("speed")
        capacity = some_dict.get("capacity")
        route = some_dict.get("route")
        if speed is None or capacity is None or route is None:
            raise ValueError("В словаре должны быть ключи speed, capacity и route")
        return cls(speed, capacity, route)


class Truck(Transport):
    """Грузовик: транспорт с грузоподъемностью"""
    def __init__(self, speed, capacity, load_capacity):
        """
        Создаёт грузовик с заданными скоростью, ёмкостью и грузоподъёмностью
        :param speed: скорость
        :param capacity: емкость
        :param load_capacity: грузоподьемность
        """
        super().__init__(speed, capacity)
        self.__load_capacity = load_capacity

    @property
    def load_capacity(self):
        """возвращает грузоподьемность грузовика"""
        return self.__load_capacity

    def delivery_cost(self, distance, price_per_km=10):
        """
        рассчитывает стоимость перевозки
        :param distance: расстояние
        :param price_per_km:цена за км (автоматически 10)
        :return:цена перевозки
        """
        return distance * price_per_km + self.load_capacity * 5

    def __str__(self):
        """возвращает строку с характеристиками грузовика, включая грузоподьемность"""
        return super().__str__() + f", грузоподъёмность: {self.load_capacity}"

    @classmethod
    def from_dict(cls, some_dict):
        """
        возвращает грузовик из словаря
        :param some_dict: словарь
        :return: новый обект класса грузовик
        :raises ValueError если нет одного из ключей
        """
        speed = some_dict.get("speed")
        capacity = some_dict.get("capacity")
        load_capacity = some_dict.get("load_capacity")
        if speed is None or capacity is None or load_capacity is None:
            raise ValueError("В словаре должны быть ключи speed, capacity и load_capacity")
        return cls(speed, capacity, load_capacity)

class Taxi(Transport):
    """Такси: транспорт с тарифом за километр"""
    def __init__(self, speed, capacity, tariff):
        """
        Создает такси с заданными скоростью, емкостью и тарифом
        :param speed: скорость
        :param capacity: емкость
        :param tariff: тариф за км
        """
        super().__init__(speed, capacity)
        self.__tariff = tariff

    @property
    def tariff(self):
        """возвращает тариф"""
        return self.__tariff

    def ride_cost(self, distance):
        """
        рассчитывает стоимость поездки
        :param distance: расстояние
        :return:стоимость поездки
        """
        return distance * self.tariff

    def __str__(self):
        """возвращает строку с характеристиками такси, включая тариф"""
        return super().__str__() + f", Тариф: {self.tariff}"

    @classmethod
    def from_dict(cls, some_dict):
        """
        создает такси из словаря
        :param some_dict: словарь
        :return: новый обьект класса такси
        :raises ValueError если нет одного из ключей
        """
        speed = some_dict.get("speed")
        capacity = some_dict.get("capacity")
        tariff = some_dict.get("tariff")
        if speed is None or capacity is None or tariff is None:
            raise ValueError("В словаре должны быть ключи speed, capacity и tariff")
        return cls(speed, capacity, tariff)

#ДЕМОНСТРАЦИЯ
# 1. Создание объектов через конструктор
t = Transport(100, 30)
bus = Bus(60, 40, "маршрут 177")
truck = Truck(70, 2, 5000)
taxi = Taxi(80, 4, 25)

print("1. Создание через конструктор:")
print(bus)
print(truck)
print(taxi)

#из словаря
print("1.2. Создание из словаря")
t1 = Transport.from_dict({"speed": 50, "capacity": 30})
b1 = Bus.from_dict({"speed": 50, "capacity": 30, "route": "№20"})
tr1 = Truck.from_dict({"speed": 70, "capacity": 2, "load_capacity": 5000})
tx1 = Taxi.from_dict({"speed": 80, "capacity": 4, "tariff": 25})

print(t1)
print(b1)
print(tr1)
print(tx1)

#2. Попытка задать недопустимую скорость
print("2. Попытка задать недопустимую скорость:")
try:
    Transport(-10, 20)
except ValueError:
    print("Недопустимое значение для скорости или емкости")


#3. вызов метода без создания объекта
print("3. вызов метода без создания объекта")
print(Transport.from_dict({"speed": 55, "capacity": 25}))


#4. полиморфный вызов метода для списка разных транспортных средств.
print("4. Полиморфный вызов метода info")
vehicles = (bus, truck, taxi)
for v in vehicles:
    print(v)





