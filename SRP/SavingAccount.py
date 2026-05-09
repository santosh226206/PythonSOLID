from abc import abstractmethod
from Account import Account

class SavingAccount(Account):

    @abstractmethod
    def withdraw(self, amount):
        pass