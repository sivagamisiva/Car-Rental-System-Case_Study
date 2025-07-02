## Car Rental System

       The Car Rental System is a terminal-based Python application designed to manage the operations of a car rental agency. It enables users to manage cars, customers, leases, and payments through a menu-driven interface using a MySQL database.

## Project Overview

       This system helps rental businesses manage their operations efficiently. Users can add and manage customer details, keep track of vehicle availability, create leases for specific time periods (daily or monthly), and record payments.  

## Technologies Used 

•	Python 3
•	MySQL
•	MySQL Connector for Python
•	Object-Oriented Programming (OOP)
•	Custom Exception Handling
•	PyCharm IDE

##  Design Principles Followed

•	Modular Design – Each feature is organized in separate packages (entity, dao, etc.)

•	OOP Concepts – Used classes, encapsulation, inheritance

•	Exception Handling – Custom exceptions for better error management

•	Interface Implementation – ICarLeaseRepository as an interface pattern  

## Features

1. Vehicle Management

•	Add, remove, or search vehicles

•	List available cars

•	Count how many leases a specific car has

2. Customer Management
 
•	Add new customers with validations

•	Update, delete, and search customers by ID

•	List all customers

3. Lease Management

•	Create new leases (Daily or Monthly)

•	Find lease by date range

•	View lease history

•	Count leases for a customer

•	Calculate lease cost

4. Payment Handling

•	Record payment for a lease

•	Show total revenue

## Validations Included

•	Email must contain @ and end with .com

•	Phone number must be exactly 10 digits

•	First and last names must only contain letters and no spaces/numbers 

## Error Handling

•	CarNotFoundException – Raised when the car ID doesn't exist

•	CustomerNotFoundException – Raised when the customer ID is invalid

•	 LeaseNotFoundException – For non-existent lease lookups


## Testing

•	Basic unit tests are placed in the test/ package

•	Includes tests for vehicle creation, lease counting, and exception handling

## Database Schema Overview

Tables Used:

•	 vehicle – Stores car details (make, model, year, rate, capacity, etc.)

•	customer – Stores customer information (name, email, phone)

•	 lease – Stores leasing details (start date, end date, lease type)

•	 payment – Stores payment records linked to lease

## Future Enhancements

1. Admin Login & Role Management
          Implement authentication and authorization to allow only admins to perform sensitive operations like deleting cars or customers.

2. Graphical User Interface (GUI)
          Replace the command-line interface with a user-friendly GUI using Tkinter or PyQt to enhance usability.

3. Lease Extension Feature
          Add functionality to allow customers to extend their lease duration and update related payment calculations.

4. Car Maintenance Module
          Track and manage vehicle maintenance history, service due dates, and availability for leasing.     

## Conclusion

       This Car Rental System project demonstrates a robust implementation of a real-world application using Python and MySQL. It follows proper modularization using packages like dao, entity, myexceptions, and util, and covers key functionalities such as customer and vehicle management, lease tracking, and payment handling.



  
