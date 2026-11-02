#!/usr/bin/env python3


import random
from abc import ABC, abstractmethod

class Person:
    """
    Класс, представляющий человека.
    """
    def __init__(self, name, gender, age):
        if not name or not isinstance(name, str):
            raise ValueError("Введите корректное имя")
        if gender.lower() not in ("м", "ж"):
            raise ValueError("Пол должен быть 'м' или 'ж'")
        if age < 0 or age > 116:
            raise ValueError("Возраст должен быть от 0 до 116 лет")
        self._name = name
        self._gender = gender
        self._age = age

    @property
    def name(self):
        """
        Возвращает имя.
        :return: Имя.
        """
        return self._name

    @property
    def age(self):
        """
        Возвращает возраст.
        :return: Возраст.
        """
        return self._age

    def get_info(self):
        """
        Возвращает полную информацию о человеке.
        :return: Строка.
        """
        return f"Человек: {self._name}, Пол: {self._gender}, Возраст: {self._age} лет"

    def is_adult(self):
        """
        Оценивает совершеннолетие (18+).
        :return: True, если 18 и больше.
        """
        return self._age >= 18

    @classmethod
    def from_variables(cls, name, gender, age):
        """
        Создает объект через переменные.
        :param name: Имя.
        :param gender: Пол.
        :param age: Возраст.
        :return: Новый объект.
        """
        return cls(name, gender, age)

class Employee(Person, ABC):
    """
    Класс сотрудника. Наследуется от Person.
    """
    def __init__(self, name, gender, age, position, salary, expenses):
        super().__init__(name, gender, age)
        if salary < 0 or expenses < 0:
            raise ValueError("Зарплата и расходы не могут быть отрицательными")
        self._position = position
        self._salary = salary
        self._expenses = expenses
        if expenses > salary:
            print(f"Сотрудник {self._name} умер, так как тратит больше, чем получает.")

    def get_info(self):
        """
        Переопределяет метод родителя, добавляя данные о работе.
        :return: Строка.
        """
        base_info = super().get_info()
        return f"{base_info}, Должность: {self._position}"

    def calculate_cash_flow(self, months):
        """
        Оценивает приток денег за N месяцев.
        :param months: Количество месяцев.
        :return: Чистый доход.
        """
        if months < 0:
            raise ValueError("Количество месяцев не может быть отрицательным")
        monthly_savings = self._salary - self._expenses
        return monthly_savings * months

    def calculate_pension_savings(self, pension_age=65):
        """
        Считает, сколько скопит денег до пенсии.
        :param pension_age: Пенсионный возраст.
        :return: Накопленная сумма.
        """
        if self._age >= pension_age:
            return 0
        years_left = pension_age - self._age
        months_left = years_left * 12
        return self.calculate_cash_flow(months_left)

    @abstractmethod
    def work(self):
        """
        У каждого человека есть работа. Абстрактный метод работы. Должен быть переопределен в дочерних классах.
        """
        pass

class Manager(Employee):
    """
    Класс менеджера.
    """
    def __init__(self, name, gender, age, salary, expenses, subordinates=None):
        super().__init__(name, gender, age, "Менеджер", salary, expenses)
        self._subordinates = subordinates if subordinates is not None else []

    def add_subordinate(self, employee_name):
        """
        Добавляет подчиненного.
        :param employee_name: Имя подчиненного.
        """
        self._subordinates.append(employee_name)

    def remove_subordinate(self, employee_name):
        """
        Удаляет подчиненного.
        :param employee_name: Имя подчиненного.
        """
        if employee_name in self._subordinates:
            self._subordinates.remove(employee_name)

    def hold_meeting(self):
        """
        Проводит митинг.
        :return: Результат митинга.
        """
        if not self._subordinates:
            return "Совещание отменено: нет подчиненных."
        return f"Менеджер {self._name} проводит совещание для: {', '.join(self._subordinates)}"

    def work(self):
        """
        Описание рабочего процесса.
        :return: Строка.
        """
        return f"Менеджер {self._name} управляет процессами."

    def get_info(self):
        """
        Переопределяет метод родителя.
        :return: Строка.
        """
        base_info = super().get_info()
        return f"{base_info}, Подчиненных: {len(self._subordinates)}"

class Developer(Employee):
    """
    Класс разработчика.
    """
    def __init__(self, name, gender, age, salary, expenses, languages=None):
        super().__init__(name, gender, age, "Разработчик", salary, expenses)
        self._languages = languages if languages is not None else ["Python"]

    def work(self):
        """
        Описание рабочего процесса.
        :return: Строка.
        """
        random_lang = random.choice(self._languages)
        return f"Разработчик {self._name} пишет код на {random_lang}."

    def get_info(self):
        """
        Переопределяет метод родителя.
        :return: Строка.
        """
        base_info = super().get_info()
        return f"{base_info}, Языки: {', '.join(self._languages)}"

class Designer(Employee):
    """
    Класс дизайнера.
    """
    def __init__(self, name, gender, age, salary, expenses, tools=None):
        super().__init__(name, gender, age, "Дизайнер", salary, expenses)
        self._tools = tools if tools is not None else ["Figma"]

    def work(self):
        """
        Описание рабочего процесса.
        :return: Строка.
        """
        return f"Дизайнер {self._name} создает макеты."

    def create_mockup(self):
        """
        Создает макет с помощью случайного инструмента.
        :return: Строка.
        """
        tool = random.choice(self._tools)
        return f"Дизайнер {self._name} создал макет в {tool}."

    def get_info(self):
        """
        Переопределяет метод родителя.
        :return: Строка.
        """
        base_info = super().get_info()
        return f"{base_info}, Инструменты: {', '.join(self._tools)}"

if __name__ == '__main__':
    print("1. Создание людей")
    person = Person("Алексей", "М", 30)
    print(person.get_info())

    print("\n2. Создание сотрудников")
    dev = Developer("Иван", "М", 25, salary=100000, expenses=40000, languages=["Python", "C++"])

    manager = Manager("Ольга", "Ж", 40, salary=150000, expenses=50000)
    manager.add_subordinate("Иван")

    bad_designer = Designer("Петя", "М", 20, salary=30000, expenses=50000)

    designer = Designer("Анна", "Ж", 22, salary=80000, expenses=30000)

    print("\n3. Финансы и пенсия")
    print(f"Иван заработает за 12 месяцев: {dev.calculate_cash_flow(12)} руб.")
    print(f"Ольга накопит до пенсии: {manager.calculate_pension_savings()} руб.")

    print("\n4. Полиморфизм (Список сотрудников)")
    employees = (dev, manager, designer)
    for emp in employees:
        print(emp.get_info())
        print("  ->", emp.work())

    print("\n5. Специфичные методы")
    print(manager.hold_meeting())
    print(designer.create_mockup())
