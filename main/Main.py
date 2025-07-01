from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from entity.Customer import Customer
from entity.Vehicle import Vehicle
from entity.Lease import Lease
from myexceptions.CarNotFoundException import CarNotFoundException
from myexceptions.LeaseNotFoundException import LeaseNotFoundException
from myexceptions.CustomerNotFoundException import CustomerNotFoundException

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
            for v in cars:
                print(f"ID: {v.get_vehicle_id()}, Make: {v.get_make()}, Model: {v.get_model()}, Year: {v.get_year()}, Rate: ₹{v.get_daily_rate()}")
        elif choice == "4":
            vid = int(input("Enter Car ID: "))
            try:
                v = service.findCarById(vid)
                print(f"ID: {v.get_vehicle_id()}, Make: {v.get_make()}, Model: {v.get_model()}, Status: {v.get_status()}")
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
            # Validate First Name
            while True:
                fname = input("First Name: ").strip()
                if fname and fname.replace(" ", "").isalpha():
                    break
                else:
                    print("Enter again.First name must contain only letters and cannot be empty.")

            # Validate Last Name
            while True:
                lname = input("Last Name: ").strip()
                if lname and lname.replace(" ", "").isalpha():
                    break
                else:
                    print("Enter again.Last name must contain only letters and cannot be empty.")

            # Validate Email
            while True:
                email = input("Email: ").strip()
                if "@" in email and email.endswith(".com"):
                    break
                else:
                    print("Invalid email format.It must contain '@' and end with '.com'.")

            # Validate Phone Number
            while True:
                phone = input("Phone Number: ").strip()
                if len(phone) == 10 and phone.isdigit():
                    break
                else:
                    print("Invalid phone number.Must be exactly 10 digits.")

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
            for c in customers:
                print(f"ID: {c.get_customer_id()}, Name: {c.get_first_name()} {c.get_last_name()}, Email: {c.get_email()}, Phone: {c.get_phone_number()}")
        elif choice == "5":
            cid = int(input("Enter Customer ID: "))
            try:
                c = service.findCustomerById(cid)
                print(f"ID: {c.get_customer_id()}, Name: {c.get_first_name()} {c.get_last_name()}, Email: {c.get_email()}, Phone: {c.get_phone_number()}")
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
            try:
                lease = service.createLease(cust_id, car_id, start, end, lease_type)
                print(f"Lease created. Lease ID: {lease.get_lease_id()}, Car ID: {lease.get_vehicle_id()}, Customer ID: {lease.get_customer_id()}")
            except Exception as e:
                print(e)
        elif choice == "2":
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            leases = service.findLease(start, end)
            if leases:
                for lease in leases:
                    print(f"Lease ID: {lease.get_lease_id()}, Vehicle ID: {lease.get_vehicle_id()}, Customer ID: {lease.get_customer_id()}, Type: {lease.get_type()}")
            else:
                print("No leases found.")
        elif choice == "3":
            leases = service.listLeaseHistory()
            for lease in leases:
                print(f"Lease ID: {lease.get_lease_id()}, Vehicle ID: {lease.get_vehicle_id()}, Customer ID: {lease.get_customer_id()}, Start: {lease.get_start_date()}, End: {lease.get_end_date()}")
        elif choice == "4":
            cust_id = int(input("Enter Customer ID: "))
            count = service.getLeaseCountByCustomer(cust_id)
            print(f"Customer {cust_id} has {count} lease(s).")

        elif choice == "5":
            car_id = int(input("Enter Car ID: "))
            count = service.getLeaseCountByCar(car_id)
            if count > 0:
                print(f"Car {car_id} has {count} lease(s).")
            else:
                print(f"No lease found for car {car_id}.")


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
            print(f"Total Revenue: ₹{total}")
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
