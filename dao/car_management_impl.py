import mysql.connector
from entity.Vehicle import Vehicle
from util.DBConn import get_connection
from exception.CarNotFoundException import CarNotFoundException
from dao.car_management_interface import ICarService

class CarServiceImpl(ICarService):

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def addCar(self, car: Vehicle) -> None:
        sql = """INSERT INTO vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (
            car.get_make(),
            car.get_model(),
            car.get_year(),
            car.get_daily_rate(),
            car.get_status(),
            car.get_passenger_capacity(),
            car.get_engine_capacity()
        )
        self.cursor.execute(sql, values)
        self.conn.commit()

    def updateCarStatus(self, carID: int, new_status: str) -> None:
        self.cursor.execute("UPDATE vehicle SET status = %s WHERE vehicleID = %s", (new_status, carID))
        self.conn.commit()

    def findCarById(self, carID: int) -> Vehicle:
        self.cursor.execute("SELECT * FROM vehicle WHERE vehicleID = %s", (carID,))
        row = self.cursor.fetchone()
        if row:
            return Vehicle(*row)
        else:
            raise CarNotFoundException(f"Car with ID {carID} not found")

    def __del__(self):
        self.cursor.close()
        self.conn.close()