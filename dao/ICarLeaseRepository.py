from abc import ABC, abstractmethod
from typing import List
from entity.Vehicle import Vehicle
from entity.Customer import Customer
from entity.Lease import Lease
from entity.Payment import Payment

class ICarLeaseRepository(ABC):
    # --- Car Management ---
    @abstractmethod
    def addCar(self, car: Vehicle) -> int: pass

    @abstractmethod
    def removeCar(self, carID: int) -> None: pass

    @abstractmethod
    def listAvailableCars(self) -> List[Vehicle]: pass

    @abstractmethod
    def findCarById(self, carID: int) -> Vehicle: pass

    # --- Customer Management ---
    @abstractmethod
    def addCustomer(self, customer: Customer) -> int: pass

    @abstractmethod
    def updateCustomerField(self, customer_id: int, field: str, new_value: str) -> None: pass

    @abstractmethod
    def removeCustomer(self, customerID: int) -> None: pass

    @abstractmethod
    def listCustomers(self) -> List[Customer]: pass

    @abstractmethod
    def findCustomerById(self, customerID: int) -> Customer: pass

    # --- Lease Management ---
    @abstractmethod
    def createLease(self, customerID: int, carID: int, startDate: str, endDate: str, lease_type: str) -> Lease: pass

    @abstractmethod
    def getLeaseCountByCustomer(self, customer_id: int) -> int: pass

    @abstractmethod
    def getLeaseCountByCar(self, car_id: int) -> int: pass

    @abstractmethod
    def listLeaseHistory(self) -> List[Lease]: pass

    @abstractmethod
    def findLease(self, start_date: str, end_date: str) -> List[Lease]: pass

    # --- Payment Management ---
    @abstractmethod
    def recordPayment(self, lease: Lease, amount: float) -> None: pass

    @abstractmethod
    def getTotalRevenue(self) -> float: pass
