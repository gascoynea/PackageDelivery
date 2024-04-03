# Truck object class
from datetime import datetime, timedelta, time


class Truck:
    def __init__(self, truck_id, package_list=[], location_at=''):
        self.truck_id = truck_id
        self.speed_mph = 18
        self.package_list = package_list
        self.start_time = timedelta(hours=8, minutes=00, seconds=00)
        self.time = timedelta(hours=8, minutes=00, seconds=00)
        self.location_at = location_at
        self.distance_travelled = 0
        self.package_list_amnt = len(package_list)
        self.truck_info = [self.truck_id, self.speed_mph, self.package_list, self.package_list_amnt, self.start_time, self.location_at]



