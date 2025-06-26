import mysql.connector
from entity.Lease import Lease
from util.DBConn import get_connection
from dao.lease_management_interface import ILeaseService

class LeaseServiceImpl(ILeaseService):

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def createLease(self, customerID: int, carID: int, startDate: str, endDate: str, lease_type: str) -> Lease:
        sql = "INSERT INTO lease (vehicleID, customerID, startDate, endDate, type) VALUES (%s, %s, %s, %s, %s)"
        values = (carID, customerID, startDate, endDate, lease_type)
        self.cursor.execute(sql, values)
        self.conn.commit()
        lease_id = self.cursor.lastrowid
        return Lease(lease_id, carID, customerID, startDate, endDate, lease_type)

    def returnCar(self, leaseID: int):
        self.cursor.execute("SELECT * FROM lease WHERE leaseID = %s", (leaseID,))
        row = self.cursor.fetchone()
        if row:
            return Lease(*row)
        else:
            print("Lease not found.")
            return None

    def calculateLeaseCost(self, leaseID: int) -> float:
            query = """
                SELECT DATEDIFF(endDate, startDate), v.dailyRate, l.type
                FROM lease l
                JOIN vehicle v ON l.vehicleID = v.vehicleID
                WHERE l.leaseID = %s
            """
            self.cursor.execute(query, (leaseID,))
            row = self.cursor.fetchone()

            if not row:
                return 0.0

            days, rate, lease_type = row
            if lease_type.lower() == 'monthly':
                months = max(1, days // 30)
                return months * rate * 25
            return days * rate

    def __del__(self):
            self.cursor.close()
            self.conn.close()