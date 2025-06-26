import unittest
from functions import create_vehicle, create_lease, get_lease_by_id, find_customer_by_id, find_car_by_id
from exception.CarNotFoundException import CarNotFoundException
from exception.CustomerNotFoundException import CustomerNotFoundException
from exception.LeaseNotFoundException import LeaseNotFoundException

class TestCarRentalSystem(unittest.TestCase):

    def setUp(self):
        print("\nSetting up test environment...")

    def test_car_created_successfully(self):
        vehicle = create_vehicle("Toyota", "Innova")
        self.assertEqual(vehicle.get_make(), "Toyota")
        self.assertEqual(vehicle.get_model(), "Innova")

    def test_lease_created_successfully(self):
        lease = create_lease(1, 1, 1)
        self.assertEqual(lease.get_lease_id(), 1)

    def test_lease_retrieved_successfully(self):
        lease = get_lease_by_id(1)
        self.assertEqual(lease.get_lease_id(), 1)

    def test_customer_not_found_exception(self):
        with self.assertRaises(CustomerNotFoundException):
            find_customer_by_id(999)

    def test_car_not_found_exception(self):
        with self.assertRaises(CarNotFoundException):
            find_car_by_id(999)

    def test_lease_not_found_exception(self):
        with self.assertRaises(LeaseNotFoundException):
            get_lease_by_id(999)

    def tearDown(self):
        print("Tearing down test environment...")

if __name__ == "__main__":
    unittest.main()
