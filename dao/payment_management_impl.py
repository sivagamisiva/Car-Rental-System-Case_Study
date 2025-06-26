import mysql.connector
from entity.Lease import Lease
from util.DBConn import get_connection
from dao.payment_management_interface import IPaymentService

class PaymentServiceImpl(IPaymentService):

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def recordPayment(self, lease: Lease, amount: float) -> None:
        sql = "INSERT INTO payment (leaseID, paymentDate, amount) VALUES (%s, CURDATE(), %s)"
        values = (lease.get_lease_id(), amount)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def getPaymentHistoryByCustomer(self, customerID: int):
        self.cursor.execute("""
            SELECT p.paymentID, p.paymentDate, p.amount, l.leaseID
            FROM payment p
            JOIN lease l ON p.leaseID = l.leaseID
            WHERE l.customerID = %s
        """, (customerID,))
        return self.cursor.fetchall()

    def getTotalRevenue(self) -> float:
        self.cursor.execute("SELECT SUM(amount) FROM payment")
        result = self.cursor.fetchone()
        return result[0] if result and result[0] else 0.0

    def __del__(self):
        self.cursor.close()
        self.conn.close()
