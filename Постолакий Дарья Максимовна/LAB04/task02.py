#!/usr/bin/env python3


DEFAULT_INTEREST_RATE = 5.0
WITHDRAW_LIMIT_PERCENT = 0.5

class BankAccount:
    """
    Класс банковского счета.
    """
    def __init__(self, owner, initial_balance=0.0):
        self._owner = owner
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self._balance = initial_balance
        self._history = []
        if initial_balance > 0:
            self._history.append(f"Открытие счета на сумму: {initial_balance}")

    @property
    def owner(self):
        """
        Возвращает владельца счета.
        :return: Имя владельца.
        """
        return self._owner

    @property
    def balance(self):
        """
        Возвращает текущий баланс.
        :return: Баланс.
        """
        return self._balance

    def get_history(self):
        """
        Возвращает копию истории операций.
        :return: Список операций.
        """
        return self._history[:]

    def deposit(self, amount):
        """
        Пополняет счет.
        :param amount: Сумма пополнения.
        :raises ValueError: Если сумма <= 0.
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")
        self._balance += amount
        self._history.append(f"Пополнение: +{amount}. Баланс: {self._balance}")

    def withdraw(self, amount):
        """
        Снимает деньги со счета.
        :param amount: Сумма снятия.
        :raises ValueError: Если сумма <= 0 или больше баланса.
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете")
        self._balance -= amount
        self._history.append(f"Снятие: -{amount}. Баланс: {self._balance}")

    @classmethod
    def create_account(cls, owner, initial_balance=0.0):
        """
        Публичный метод для создания объекта (альтернативный конструктор).
        :param owner: Имя владельца.
        :param initial_balance: Начальный баланс.
        :return: Новый объект счета.
        """
        return cls(owner, initial_balance)

class SavingsAccount(BankAccount):
    """
    Класс сберегательного счета. Наследуется от BankAccount.
    """
    def __init__(self, owner, initial_balance=0.0, interest_rate=DEFAULT_INTEREST_RATE):
        super().__init__(owner, initial_balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        """
        Возвращает процентную ставку.
        :return: Ставка в процентах.
        """
        return self._interest_rate

    def apply_interest(self):
        """
        Начисляет проценты на текущий баланс.
        """
        interest_amount = self.balance * (self._interest_rate / 100)
        self.deposit(interest_amount)

    def withdraw(self, amount):
        """
        Переопределенный метод снятия (не более 50% баланса).
        :param amount: Сумма снятия.
        :raises ValueError: Если сумма превышает 50% баланса.
        """
        max_withdraw = self.balance * WITHDRAW_LIMIT_PERCENT
        if amount > max_withdraw:
            raise ValueError(f"Нельзя снять больше {WITHDRAW_LIMIT_PERCENT * 100}% баланса (максимум {max_withdraw})")
        super().withdraw(amount) # если проверка прошла, вызываем метод родителя (он сделает остальные проверки)

if __name__ == '__main__':
    print("1. Корректные операции")
    account = BankAccount.create_account("Иван", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Баланс Ивана: {account.balance}")

    print("\n2. Ошибки при операциях")
    try:
        account.deposit(-100)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        account.withdraw(5000)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n3. Невозможность изменить баланс напрямую")
    try:
        account.balance = 100000
    except AttributeError as e:
        print("Ошибка: Нельзя изменить баланс напрямую! (нет сеттера)")

    print("\n4. История операций")
    for record in account.get_history():
        print(record)

    print("\n5. Полиморфизм и сберегательный счет")
    savings = SavingsAccount("Мария", 2000, 10.0)

    print(f"Баланс Марии до процентов: {savings.balance}")
    savings.apply_interest()
    print(f"Баланс Марии после начисления 10%: {savings.balance}")

    accounts = (account, savings)

    print("\n6. Снятие 1500")
    for acc in accounts:
        try:
            print(f"Счет {acc.owner} (баланс {acc.balance}): пытаемся снять 1500...")
            acc.withdraw(1500)
            print(f"Успешно! Новый баланс: {acc.balance}")
        except ValueError as e:
            print(f"Отказ для {acc.owner}: {e}")

    print("\n7. Снятие 500")
    for acc in accounts:
        try:
            print(f"Счет {acc.owner} (баланс {acc.balance}): пытаемся снять 500...")
            acc.withdraw(500)
            print(f"Успешно! Новый баланс: {acc.balance}")
        except ValueError as e:
            print(f"Отказ для {acc.owner}: {e}")
