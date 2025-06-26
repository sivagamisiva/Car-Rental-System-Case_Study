from entity.Vehicle import Vehicle
from entity.Lease import Lease
from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.LeaseNotFoundException import LeaseNotFoundException

def create_vehicle(make, model):
    if make and model:
        return Vehicle(1, make, model, 2024, 3000.0, "available", 5, 1500)
    else:
        raise ValueError("Invalid vehicle data")

def create_lease(lease_id, vehicle_id, customer_id):
    if lease_id > 0:
        return Lease(lease_id, vehicle_id, customer_id, "2025-07-01", "2025-07-05", "Daily")
    else:
        raise ValueError("Invalid lease ID")

def get_lease_by_id(lease_id):
    if lease_id == 1:
        return Lease(1, 1, 1, "2025-07-01", "2025-07-05", "Daily")
    else:
        raise LeaseNotFoundException("Lease ID not found")

def find_customer_by_id(customer_id):
    if customer_id != 999:
        return True
    else:
        raise CustomerNotFoundException("Customer not found")

def find_car_by_id(car_id):
    if car_id != 999:
        return True
    else:
        raise CarNotFoundException("Car not found")
