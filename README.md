## Car Rental System
The Car Rental System is a terminal-based Python application designed to manage the operations of a car rental agency. It enables users to manage cars, customers, leases, and payments through a menu-driven interface using a MySQL database.

## Project Overview
This system helps rental businesses manage their operations efficiently. Users can add and manage customer details, keep track of vehicle availability, create leases for specific time periods (daily or monthly), and record payments.

## Technologies Used

    - Python 3
    - MySQL
    - MySQL Connector for Python
    - Object-Oriented Programming (OOP)
    - Custom Exception Handling
    - PyCharm IDE (recommended)

##  Design Principles Followed

    --> Modular Design – Each feature is organized in separate packages (entity, dao, etc.)

    --> OOP Concepts – Used classes, encapsulation, inheritance

    --> Exception Handling – Custom exceptions for better error management

    --> Interface Implementation – ICarLeaseRepository as an interface pattern  

## Features

 Vehicle Management

      - Add, remove, or search vehicles

      - List available cars

      - Count how many leases a specific car has

 Customer Management
 
      - Add new customers with validations

      - Update, delete, and search customers by ID

      - List all customers

Lease Management

       - Create new leases (Daily or Monthly)

       - Find lease by date range

       - View lease history

       - Count leases for a customer

       - Calculate lease cost

Payment Handling

       - Record payment for a lease

       - Show total revenue

## Validations Included

      -> Email must contain @ and end with .com

      -> Phone number must be exactly 10 digits

      -> First and last names must only contain letters and no spaces/numbers 

## Error Handling

    < CarNotFoundException – Raised when the car ID doesn't exist

    < CustomerNotFoundException – Raised when the customer ID is invalid

    < LeaseNotFoundException – For non-existent lease lookups


## Testing

    > Basic unit tests are placed in the test/ package

    > Includes tests for vehicle creation, lease counting, and exception handling

## Database Schema Overview

# Tables Used:

     ..> vehicle – Stores car details (make, model, year, rate, capacity, etc.)

     ..> customer – Stores customer information (name, email, phone)

     ..> lease – Stores leasing details (start date, end date, lease type)

     ..> payment – Stores payment records linked to lease

## Steps to Run the Project:

   - Clone this repository to another system

   - Set up a MySQL database with tables for vehicle, customer, lease, and payment

   - Edit the database connection details in DBConnUtil.py

   - Then right-click main and select run

  

