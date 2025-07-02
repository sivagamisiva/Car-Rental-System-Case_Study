from dao.ICarLeaseRepository import ICarLeaseRepository
from entity.Vehicle import Vehicle
from entity.Customer import Customer
from entity.Lease import Lease
from entity.Payment import Payment
from util.DBConnUtil import DBConnUtil
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.CustomerNotFoundException import CustomerNotFoundException

class ICarLeaseRepositoryImpl(ICarLeaseRepository):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    # --- Car Management ---
    def addCar(self, car: Vehicle) -> int:
        sql = """INSERT INTO vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (
            car.get_make(), car.get_model(), car.get_year(), car.get_daily_rate(),
            car.get_status(), car.get_passenger_capacity(), car.get_engine_capacity()
        )
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def removeCar(self, carID: int) -> None:
        self.cursor.execute("DELETE FROM vehicle WHERE vehicleID = %s", (carID,))
        self.conn.commit()

    def listAvailableCars(self):
        self.cursor.execute("SELECT * FROM vehicle WHERE status = 'available'")
        return [Vehicle(*row) for row in self.cursor.fetchall()]

    def findCarById(self, carID: int) -> Vehicle:
        self.cursor.execute("SELECT * FROM vehicle WHERE vehicleID = %s", (carID,))
        row = self.cursor.fetchone()
        if row:
            return Vehicle(*row)
        else:
            raise CarNotFoundException(f"Car with ID {carID} not found")

    # --- Customer Management ---
    def addCustomer(self, customer: Customer) -> int:
        sql = "INSERT INTO customer (firstName, lastName, email, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (
            customer.get_first_name(), customer.get_last_name(),
            customer.get_email(), customer.get_phone_number()
        )
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def updateCustomerField(self, customer_id: int, field: str, new_value: str) -> None:
        allowed_fields = ["firstName", "lastName", "email", "phoneNumber"]
        if field not in allowed_fields:
            raise ValueError("Invalid field for update.")
        sql = f"UPDATE customer SET {field} = %s WHERE customerID = %s"
        self.cursor.execute(sql, (new_value, customer_id))
        self.conn.commit()

    def removeCustomer(self, customerID: int) -> None:
        self.cursor.execute("DELETE FROM customer WHERE customerID = %s", (customerID,))
        self.conn.commit()

    def listCustomers(self):
        self.cursor.execute("SELECT * FROM customer")
        return [Customer(*row) for row in self.cursor.fetchall()]

    def findCustomerById(self, customerID: int) -> Customer:
        self.cursor.execute("SELECT * FROM customer WHERE customerID = %s", (customerID,))
        row = self.cursor.fetchone()
        if row:
            return Customer(*row)
        else:
            raise CustomerNotFoundException(f"Customer with ID {customerID} not found")

    # --- Lease Management ---
    def createLease(self, customerID: int, carID: int, startDate: str, endDate: str, lease_type: str) -> Lease:
        sql = "INSERT INTO lease (vehicleID, customerID, startDate, endDate, type) VALUES (%s, %s, %s, %s, %s)"
        values = (carID, customerID, startDate, endDate, lease_type)
        self.cursor.execute(sql, values)
        self.conn.commit()
        lease_id = self.cursor.lastrowid
        return Lease(lease_id, carID, customerID, startDate, endDate, lease_type)

    def listLeaseHistory(self):
        self.cursor.execute("SELECT * FROM lease")
        return [Lease(*row) for row in self.cursor.fetchall()]

    def getLeaseCountByCustomer(self, customer_id: int) -> int:
        sql = "SELECT COUNT(*) FROM lease WHERE customerID = %s"
        self.cursor.execute(sql, (customer_id,))
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def getLeaseCountByCar(self, car_id: int) -> int:
        sql = "SELECT COUNT(*) FROM lease WHERE vehicleID = %s"
        self.cursor.execute(sql, (car_id,))
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def findLease(self, start_date: str, end_date: str):
        sql = """
            SELECT * FROM lease
            WHERE startDate = %s AND endDate = %s
        """
        values = (start_date, end_date)
        self.cursor.execute(sql, values)
        rows = self.cursor.fetchall()
        leases = [Lease(*row) for row in rows]
        return leases

    # --- Payment Handling ---
    def recordPayment(self, lease: Lease, amount: float) -> None:
        sql = "INSERT INTO payment (leaseID, paymentDate, amount) VALUES (%s, CURDATE(), %s)"
        values = (lease.get_lease_id(), amount)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def getTotalRevenue(self) -> float:
        sql = "SELECT SUM(amount) FROM payment"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()[0]
        return result if result is not None else 0.0

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
