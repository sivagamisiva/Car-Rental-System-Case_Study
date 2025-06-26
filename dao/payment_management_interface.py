from abc import ABC, abstractmethod
from entity.Lease import Lease

class IPaymentService(ABC):

    @abstractmethod
    def recordPayment(self, lease: Lease, amount: float) -> None:
        pass

    @abstractmethod
    def getPaymentHistoryByCustomer(self, customerID: int):
        pass

    @abstractmethod
    def getTotalRevenue(self) -> float:
        pass