from abc import ABC, abstractmethod
from entity.Vehicle import Vehicle

class ICarService(ABC):

    @abstractmethod
    def addCar(self, car: Vehicle) -> None:
        pass

    @abstractmethod
    def updateCarStatus(self, carID: int, new_status: str) -> None:
        pass

    @abstractmethod
    def findCarById(self, carID: int) -> Vehicle:
        pass