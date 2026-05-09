from typing import override

from exception.InsufficientBalanceException import InsufficientBalanceException
from SavingAccount import SavingAccount


# Custom Exception
# class InsufficientBalanceException(Exception):
#     pass


class ConcreteSavingAccount(SavingAccount):

    def __init__(self):
        self.amount = 0
    @override
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.amount += amount
    @override
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0")

        if amount > self.amount:
            raise InsufficientBalanceException(
                "Insufficient balance in account"
            )

        self.amount -= amount

    def __str__(self):
        return f"Balance = {self.amount}"