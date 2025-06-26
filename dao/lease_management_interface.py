from abc import ABC, abstractmethod
from entity.Lease import Lease

class ILeaseService(ABC):

    @abstractmethod
    def createLease(self, customerID: int, carID: int, startDate: str, endDate: str, lease_type: str) -> Lease:
        pass

    @abstractmethod
    def returnCar(self, leaseID: int) -> Lease:
        pass
    @abstractmethod
    def calculateLeaseCost(self, leaseID: int) -> float:
        pass