from datetime import date, timedelta

from ..battery import Battery


class SpindlerBattery(Battery):

    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return timedelta(years=2) <= self.current_date - self.last_service_date