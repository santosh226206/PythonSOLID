

# This class is basically a made to test the SPR of Solid principle.
# it basically contains only one mehod to deposit amount
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass