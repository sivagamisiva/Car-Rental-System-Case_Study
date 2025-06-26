from abc import ABC, abstractmethod
from entity.Customer import Customer

class ICustomerService(ABC):

    @abstractmethod
    def addCustomer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def updateCustomer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def findCustomerById(self, customerID: int) -> Customer:
        pass