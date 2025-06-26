from dao.car_management_impl import CarServiceImpl
from dao.customer_management_impl import CustomerServiceImpl
from dao.lease_management_impl import LeaseServiceImpl
from dao.payment_management_impl import PaymentServiceImpl

from entity.Customer import Customer
from entity.Vehicle import Vehicle

def MainModule():
    car_service = CarServiceImpl()
    customer_service = CustomerServiceImpl()
    lease_service = LeaseServiceImpl()
    payment_service = PaymentServiceImpl()

    while True:
        print("\n===== Car Rental System Menu =====")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Find Customer By ID")
        print("4. Add Vehicle")
        print("5. Update Car Status")
        print("6. Find Car By ID")
        print("7. Create Lease")
        print("8. Calculate Lease Cost")
        print("9. Record Payment")
        print("10. Payment History by Customer")
        print("11. Total Revenue")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            customer = Customer(None, fname, lname, email, phone)
            customer_service.addCustomer(customer)
            print("New Customer added.")

        elif choice == "2":
            cid = int(input("Customer ID to update: "))
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            customer = Customer(cid, fname, lname, email, phone)
            customer_service.updateCustomer(customer)
            print("Customer information updated.")

        elif choice == "3":
            cid = int(input("Enter Customer ID: "))
            customer = customer_service.findCustomerById(cid)
            print(customer.get_customer_id(), customer.get_first_name(), customer.get_last_name(), customer.get_email(), customer.get_phone_number())

        elif choice == "4":
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            rate = float(input("Daily Rate: "))
            status = input("Status (available/notAvailable): ")
            pc = int(input("Passenger Capacity: "))
            ec = int(input("Engine Capacity: "))
            vehicle = Vehicle(None, make, model, year, rate, status, pc, ec)
            car_service.addCar(vehicle)
            print("New Vehicle added.")

        elif choice == "5":
            car_id = int(input("Enter Car ID to update: "))
            new_status = input("Enter New Status (available/notAvailable): ")
            car_service.updateCarStatus(car_id, new_status)
            print("Car status updated.")

        elif choice == "6":
            car_id = int(input("Enter Car ID: "))
            car = car_service.findCarById(car_id)
            print(car.get_vehicle_id(), car.get_make(), car.get_model(), car.get_status())

        elif choice == "7":
            cust_id = int(input("Enter Customer ID: "))
            car_id = int(input("Enter Car ID: "))
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            lease_type = input("Lease Type (Daily/Monthly): ")
            lease = lease_service.createLease(cust_id, car_id, start, end, lease_type)
            print("Lease created with ID:", lease.get_lease_id())

        elif choice == "8":
            lease_id = int(input("Enter Lease ID: "))
            cost = lease_service.calculateLeaseCost(lease_id)
            print(f"Total Lease Cost: ₹{cost:.2f}")

        elif choice == "9":
            lease_id = int(input("Lease ID: "))
            amount = float(input("Amount: "))
            lease = lease_service.returnCar(lease_id)
            payment_service.recordPayment(lease, amount)
            print("Payment recorded.")

        elif choice == "10":
            cust_id = int(input("Enter Customer ID: "))
            payments = payment_service.getPaymentHistoryByCustomer(cust_id)
            print("\n--- Payment History ---")
            for p in payments:
                print(f"Payment ID: {p[0]}, Date: {p[1]}, Amount: ₹{p[2]}, Lease ID: {p[3]}")
        elif choice == "11":
            revenue = payment_service.getTotalRevenue()
            print(f"Total Revenue: ₹{revenue:.2f}")

        elif choice == "12":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    MainModule()