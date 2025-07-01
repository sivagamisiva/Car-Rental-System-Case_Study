from util.DBConnUtil import get_connection
conn = get_connection()
if conn is None:
    print("Failed to connect to the database. Exiting.")
    exit()

cursor = conn.cursor()
with open(r"C:\Users\sivag\PycharmProjects\CarRentalSystem\DB\create_tables.txt", "r") as f:
    sql_script = f.read()

for statement in sql_script.split(";"):
    if statement.strip():
        cursor.execute(statement.strip() + ";")

print("Tables created successfully.")

customer_data = [
    ('Siva', 'Kumar', 'siva1@example.com', '9876543210'),
    ('Meena', 'Rani', 'meena2@example.com', '9898989898'),
    ('Arjun', 'Raj', 'arjun3@example.com', '9123456780'),
    ('Divya', 'Shree', 'divya4@example.com', '9012345678'),
    ('Vimal', 'Das', 'vimal5@example.com', '9001122334'),
    ('Pooja', 'Verma', 'pooja6@example.com', '9900112233'),
    ('Rahul', 'Shah', 'rahul7@example.com', '9988776655'),
    ('Neha', 'Nair', 'neha8@example.com', '9765432100'),
    ('Amit', 'Roy', 'amit9@example.com', '9090909090'),
    ('Kavya', 'Menon', 'kavya10@example.com', '9555567890')
]
cursor.executemany(
    "INSERT INTO customer (firstName, lastName, email, phoneNumber) VALUES (%s, %s, %s, %s)",
   customer_data
)
print("Customer records inserted.")


vehicle_data = [
    ('Toyota', 'Innova', 2020, 3000.0, 'not available', 7, 2400),
    ('Toyota', 'Innova', 2021, 3200.0, 'available', 7, 2400),
    ('Honda', 'City', 2021, 2500.0, 'not available', 5, 1500),
    ('Honda', 'City', 2022, 2700.0, 'not available', 5, 1500),
    ('Tata', 'Nexon', 2022, 2600.0, 'available', 5, 1200),
    ('Hyundai', 'Creta', 2019, 2800.0, 'not available', 5, 1600),
    ('Mahindra', 'XUV700', 2023, 3200.0, 'available', 7, 2200),
    ('Mahindra', 'XUV700', 2023, 3300.0, 'not available', 7, 2200),
    ('Hyundai', 'Venue', 2020, 2400.0, 'not available', 5, 1400),
    ('Suzuki', 'Brezza', 2021, 2350.0, 'available', 5, 1300)
]
cursor.executemany(
    """INSERT INTO vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
       VALUES (%s, %s, %s, %s, %s, %s, %s)""",
    vehicle_data
)
print("Vehicle records inserted.")

lease_data = [
    (1, 1, '2025-07-01', '2025-07-05', 'Daily'),
    (2, 2, '2025-07-01', '2025-07-05', 'Daily'),
    (3, 3, '2025-07-02', '2025-07-06', 'Monthly'),
    (4, 4, '2025-07-03', '2025-07-07', 'Monthly'),
    (5, 5, '2025-07-01', '2025-07-05', 'Daily'),
    (6, 6, '2025-07-04', '2025-07-09', 'Monthly'),
    (7, 7, '2025-07-01', '2025-07-05', 'Daily'),
    (8, 8, '2025-07-05', '2025-07-10', 'Monthly'),
    (9, 9, '2025-07-06', '2025-07-11', 'Daily'),
    (10, 10, '2025-07-07', '2025-07-12', 'Monthly')
]
cursor.executemany(
    "INSERT INTO lease (vehicleID, customerID, startDate, endDate, type) VALUES (%s, %s, %s, %s, %s)",
   lease_data
)
print("Lease records inserted.")


payment_data = [
    (1, '2025-07-01', 12000.0),
    (2, '2025-07-01', 10000.0),
    (3, '2025-07-02', 22000.0),
    (4, '2025-07-03', 11000.0),
    (5, '2025-07-01', 25000.0),
    (6, '2025-07-04', 17000.0),
    (7, '2025-07-01', 16000.0),
    (8, '2025-07-05', 18000.0),
    (9, '2025-07-06', 14000.0),
    (10, '2025-07-07', 19000.0)
]
cursor.executemany(
   "INSERT INTO payment (leaseID, paymentDate, amount) VALUES (%s, %s, %s)",
  payment_data
)
print("Payment records inserted.")

conn.commit()
cursor.close()
conn.close()
print("All records committed and connection closed.")
