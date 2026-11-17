class BankAccount:
    """Банковский счёт с балансом, владельцем и историей операций."""

    def __init__(self, owner, balance=0):
        """
        Создает аккаунт с именем владельцаи и балансом
        :param owner: Имя владельца, не пустая строка
        :param balance: баланс
        """
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Владелец должен быть непустой строкой")
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self._owner = owner
        self._balance = balance
        self._history = []
        if balance > 0:
            self._history.append(f"Открытие счёта: {balance}")

    @property
    def owner(self):
        """узнать владелльца"""
        return self._owner

    @property
    def balance(self):
        """узнать баланс"""
        return self._balance

    def get_history(self):
        """Возвращает копию истории, а не внутренний список"""
        return list(self._history)

    def _validate_amount(self, amount):
        """Проверяет сумму на правильность значения"""
        if type(amount) not in (int, float):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")

    def deposit(self, amount):
        """
        Пополняет счёт на сумму (amount)
        :param amount: сумма пополнения
        """
        self._validate_amount(amount)
        self._balance += amount
        self._history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        """
        Снимает сумму со счёта
        :param amount: сумма снятия
        """
        self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        self._history.append(f"Снятие: -{amount}")

    @classmethod
    def create(cls, owner, balance=0):
        """возможность создать объект класса при помощи публичного метода"""
        return cls(owner, balance)

    def __str__(self):
        """выводит строку с информацией о аккаунте"""
        return f"Владелец: {self.owner}, Баланс: {self.balance}"


DEFAULT_INTEREST_RATE = 5

class SavingsAccount(BankAccount):
    """Сберегательный счёт: процентная ставка + переопределяет метод снятия, нельзя снять более 50% баланса за одну операцию."""

    def __init__(self, owner, balance=0, interest_rate= DEFAULT_INTEREST_RATE):
        """
        :param owner: владелец
        :param balance: баланс, автоматически 0
        :param interest_rate: процентная ставка, DEFAULT_INTEREST_RATE = 5
        """
        super().__init__(owner, balance)
        if interest_rate <= 0:
            raise ValueError("Процентная ставка должна быть больше 0")
        self.__interest_rate = interest_rate

    @property
    def interest_rate(self):
        """возвращает процентную ставку"""
        return self.__interest_rate

    def apply_interest(self):
        """начисляет проценты на текущий баланс через deposit()"""
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)

    def withdraw(self, amount):
        """Нельзя снять больше 50% баланса за операцию"""
        self._validate_amount(amount)
        limit = self.balance * 0.5
        if amount > limit:
            raise ValueError(
                f"Со сберегательного счёта можно снять не более "
                f"{limit} (50% баланса) за операцию"
            )
        super().withdraw(amount)


#ДЕМОНСТРАЦИЯ

#1.корректные пополнение и снятие и вывод истории операций (4)
print("1. Корректные операции:")
acc = BankAccount.create("Иван", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc)
print(f"Вывод истории операций: \n{acc.get_history()}")

#2. ошибки при отрицательной сумме и превышении баланса;
print("2. Oшибки при отрицательной сумме и превышении баланса;")
try:
    acc.deposit(-100)
except ValueError as e:
    print(f"  deposit(-100): {e}")

try:
    acc.withdraw(1000000000)
except ValueError as e:
    print(f"  withdraw(1000000000): {e}")

# 3. Невозможность изменить баланс напрямую
try:
    acc.balance = 1000000000000000
except AttributeError as e:
    print(f"Невозможно изменить баланс напрямую: {e}")


#5.полиморфное поведение метода снятия денег для обычного и сберегательного счёта.
regular = BankAccount.create("Пётр", 1000)
savings = SavingsAccount("Мария", 1000, interest_rate=10)
for a in [regular, savings]:
    try:
        a.withdraw(700)
        print(f"{type(a).__name__}: сняли 700, баланс {a.balance}")
    except ValueError as e:
        print(f"{type(a).__name__}: {e}")










