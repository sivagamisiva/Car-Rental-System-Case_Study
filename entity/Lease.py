class Lease:
    def __init__(self, lease_id=None, vehicle_id=None, customer_id=None, start_date=None, end_date=None, lease_type=None):
        self.__lease_id = lease_id
        self.__vehicle_id = vehicle_id
        self.__customer_id = customer_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__lease_type = lease_type

    # Getters
    def get_lease_id(self):
        return self.__lease_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_customer_id(self):
        return self.__customer_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_type(self):
        return self.__lease_type

    # Setters
    def set_lease_id(self, lease_id):
        self.__lease_id = lease_id

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_type(self, lease_type):
        self.__lease_type = lease_type
