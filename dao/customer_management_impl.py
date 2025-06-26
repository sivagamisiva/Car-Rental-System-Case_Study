import mysql.connector
from entity.Customer import Customer
from util.DBConn import get_connection
from exception.CustomerNotFoundException import CustomerNotFoundException
from dao.customer_management_interface import ICustomerService

class CustomerServiceImpl(ICustomerService):

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def addCustomer(self, customer: Customer) -> None:
        sql = "INSERT INTO customer (firstName, lastName, email, phoneNumber) VALUES (%s, %s, %s, %s)"
        values = (
            customer.get_first_name(),
            customer.get_last_name(),
            customer.get_email(),
            customer.get_phone_number()
        )
        self.cursor.execute(sql, values)
        self.conn.commit()

    def updateCustomer(self, customer: Customer) -> None:
        sql = "UPDATE customer SET firstName = %s, lastName = %s, email = %s, phoneNumber = %s WHERE customerID = %s"
        values = (
            customer.get_first_name(),
            customer.get_last_name(),
            customer.get_email(),
            customer.get_phone_number(),
            customer.get_customer_id()
        )
        self.cursor.execute(sql, values)
        self.conn.commit()

    def findCustomerById(self, customerID: int) -> Customer:
        self.cursor.execute("SELECT * FROM customer WHERE customerID = %s", (customerID,))
        row = self.cursor.fetchone()
        if row:
            return Customer(*row)
        else:
            raise CustomerNotFoundException(f"Customer with ID {customerID} not found")

    def __del__(self):
        self.cursor.close()
        self.conn.close()