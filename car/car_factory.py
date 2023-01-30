from datetime import date

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from car import Car


class CarFactory:
    
    @staticmethod
    def create_calliope(self, current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date))
        
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage),
                   SpindlerBattery(last_service_date, current_date))

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date,
                          warning_light_on: bool):
        return Car(SternmanEngine(warning_light_on),
                   SpindlerBattery(last_service_date, current_date))
        
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date,
                         current_mileage: int, last_service_mileage: int):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage),
                   NubbinBattery(last_service_date, current_date))
        
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int):
        return Car(CapuletEngine(last_service_mileage, current_mileage),
                   NubbinBattery(last_service_date, current_date))
