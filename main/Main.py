from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.Customer import Customer
from entity.Vehicle import Vehicle
from entity.Lease import Lease
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.LeaseNotFoundException import LeaseNotFoundException
from myexceptions.CustomerNotFoundException import CustomerNotFoundException
from tabulate import tabulate

def update_customer_info(service):
    try:
        customer_id = int(input("Enter Customer ID to update: "))
        print("What do you want to update?")
        print("1. First Name")
        print("2. Last Name")
        print("3. Email")
        print("4. Phone Number")
        choice = input("Enter choice (1-4): ")
        if choice == "1":
            new_fname = input("Enter new first name: ").strip()
            if new_fname and new_fname.replace(" ", "").isalpha():
                service.updateCustomerField(customer_id, "firstName", new_fname)
                print("First name updated.")
            else:
                print("Invalid name.")
        elif choice == "2":
            new_lname = input("Enter new last name: ").strip()
            if new_lname and new_lname.replace(" ", "").isalpha():
                service.updateCustomerField(customer_id, "lastName", new_lname)
                print("Last name updated.")
            else:
                print("Invalid name.")
        elif choice == "3":
            new_email = input("Enter new email: ").strip()
            if "@" in new_email and new_email.endswith(".com"):
                service.updateCustomerField(customer_id, "email", new_email)
                print("Email updated.")
            else:
                print("Invalid email.")
        elif choice == "4":
            new_phone = input("Enter new phone number (10 digits): ").strip()
            if new_phone.isdigit() and len(new_phone) == 10:
                service.updateCustomerField(customer_id, "phoneNumber", new_phone)
                print("Phone number updated.")
            else:
                print("Invalid phone number.")
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Error updating customer info:", e)

def car_management(service):
    while True:
        print("\n--- Car Management ---")
        print("1. Add Car")
        print("2. Remove Car")
        print("3. List Available Cars")
        print("4. Find Car by ID")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            rate = float(input("Daily Rate: "))
            status = input("Status (available/notAvailable): ")
            pc = int(input("Passenger Capacity: "))
            ec = int(input("Engine Capacity: "))
            vehicle = Vehicle(None, make, model, year, rate, status, pc, ec)
            vehicle_id = service.addCar(vehicle)
            print(f"Car added with ID: {vehicle_id}")

        elif choice == "2":
            vid = int(input("Enter Car ID to remove: "))
            try:
                service.removeCar(vid)
                print("Car removed.")
            except CarNotFoundException as e:
                print(e)

        elif choice == "3":
            cars = service.listAvailableCars()
            headers = ["ID", "Make", "Model", "Year", "Rate", "Status"]
            rows = [[v.get_vehicle_id(), v.get_make(), v.get_model(), v.get_year(), f"₹{v.get_daily_rate():.2f}", v.get_status()] for v in cars]
            print(tabulate(rows, headers=headers, tablefmt="grid"))

        elif choice == "4":
            vid = int(input("Enter Car ID: "))
            try:
                v = service.findCarById(vid)
                headers = ["ID", "Make", "Model", "Status"]
                rows = [[v.get_vehicle_id(), v.get_make(), v.get_model(), v.get_status()]]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            except CarNotFoundException as e:
                print(e)

        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def customer_management(service):
    while True:
        print("\n--- Customer Management ---")
        print("1. Add Customer")
        print("2. Update Customer Info")
        print("3. Remove Customer")
        print("4. List Customers")
        print("5. Find Customer by ID")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            fname = input("First Name: ").strip()
            lname = input("Last Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone Number: ").strip()
            customer = Customer(None, fname, lname, email, phone)
            cid = service.addCustomer(customer)
            print(f"Customer created with ID: {cid}")

        elif choice == "2":
            update_customer_info(service)

        elif choice == "3":
            cid = int(input("Enter Customer ID to remove: "))
            service.removeCustomer(cid)
            print("Customer removed.")

        elif choice == "4":
            customers = service.listCustomers()
            headers = ["ID", "Name", "Email", "Phone"]
            rows = [[c.get_customer_id(), f"{c.get_first_name()} {c.get_last_name()}", c.get_email(), c.get_phone_number()] for c in customers]
            print(tabulate(rows, headers=headers, tablefmt="grid"))

        elif choice == "5":
            cid = int(input("Enter Customer ID: "))
            try:
                c = service.findCustomerById(cid)
                headers = ["ID", "Name", "Email", "Phone"]
                row = [[c.get_customer_id(), f"{c.get_first_name()} {c.get_last_name()}", c.get_email(), c.get_phone_number()]]
                print(tabulate(row, headers=headers, tablefmt="grid"))
            except CustomerNotFoundException as e:
                print(e)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

def lease_management(service):
    while True:
        print("\n--- Lease Management ---")
        print("1. Create Lease")
        print("2. Find Lease")
        print("3. List Lease History")
        print("4. Lease Count by Customer")
        print("5. Check Lease for Car")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            cust_id = int(input("Customer ID: "))
            car_id = int(input("Car ID: "))
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            lease_type = input("Lease Type (daily/monthly): ")
            lease = service.createLease(cust_id, car_id, start, end, lease_type)
            headers = ["LeaseID", "VehicleID", "CustomerID", "Type"]
            row = [[lease.get_lease_id(), lease.get_vehicle_id(), lease.get_customer_id(), lease.get_type()]]
            print(tabulate(row, headers=headers, tablefmt="grid"))

        elif choice == "2":
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            leases = service.findLease(start, end)
            headers = ["LeaseID", "VehicleID", "CustomerID", "Type"]
            rows = [[l.get_lease_id(), l.get_vehicle_id(), l.get_customer_id(), l.get_type()] for l in leases]
            print(tabulate(rows, headers=headers, tablefmt="grid"))

        elif choice == "3":
            leases = service.listLeaseHistory()
            headers = ["LeaseID", "VehicleID", "CustomerID", "Start", "End"]
            rows = [[l.get_lease_id(), l.get_vehicle_id(), l.get_customer_id(), l.get_start_date(), l.get_end_date()] for l in leases]
            print(tabulate(rows, headers=headers, tablefmt="grid"))

        elif choice == "4":
            cust_id = int(input("Enter Customer ID: "))
            count = service.getLeaseCountByCustomer(cust_id)
            print(f"Customer {cust_id} has {count} lease(s).")

        elif choice == "5":
            car_id = int(input("Enter Car ID: "))
            count = service.getLeaseCountByCar(car_id)
            print(f"Car {car_id} has {count} lease(s).")

        elif choice == "6":
            break
        else:
            print("Invalid choice.")

def payment_management(service):
    while True:
        print("\n--- Payment Management ---")
        print("1. Record Payment")
        print("2. Total Revenue")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            lease_id = int(input("Enter Lease ID: "))
            amount = float(input("Enter Payment Amount: "))
            lease = Lease(lease_id)
            service.recordPayment(lease, amount)
            print("Payment recorded.")

        elif choice == "2":
            total = service.getTotalRevenue()
            headers = ["Total Revenue"]
            rows = [[f"₹{float(total):,.2f}"]]
            print(tabulate(rows, headers=headers, tablefmt="grid"))

        elif choice == "3":
            break
        else:
            print("Invalid choice.")

def MainModule():
    service = ICarLeaseRepositoryImpl()
    while True:
        print("\n===== Car Rental System Main Menu =====")
        print("1. Car Management")
        print("2. Customer Management")
        print("3. Lease Management")
        print("4. Payment Management")
        print("5. Exit")
        choice = input("Enter your choice:  ")
        if choice == "1":
            car_management(service)
        elif choice == "2":
            customer_management(service)
        elif choice == "3":
            lease_management(service)
        elif choice == "4":
            payment_management(service)
        elif choice == "5":
            print("Exiting system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    MainModule()