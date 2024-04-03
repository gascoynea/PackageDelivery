# Package object class
from datetime import datetime, timedelta, time

class Package:

    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, weight_kgs, notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight_kgs = weight_kgs
        self.notes = notes
        self.status = status
        self.delivered_time = timedelta(hours=8, minutes=00, seconds=00)
        self.package_total = [self.package_id, self.address, self.city, self.state, self.zipcode,
                              self.delivery_deadline, self.weight_kgs, self.notes, self.status, self.delivered_time]

    # Used to update status form user input
    def update_status(self, time):
        if self.delivered_time < time:
            self.status = "Delivered"
        elif self.delivered_time > time:
            self.status = "En route"
        else:
            self.status = "At Hub"