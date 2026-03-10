class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        raise ValueError("Depozit məbləği müsbət olmalıdır")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Kifayət qədər vəsait yoxdur")
        self.balance -= amount
        return self.balance

    def show_balance(self):
        return self.balance
