import sys
sys.path.append("C:\\Programming\\forage-lyft-starter-repo-1\\src")

import unittest
from datetime import date, timedelta

from car.utils.car_factory import CarFactory


class Tests(unittest.TestCase):
    
    def test_calliope_battery_true_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 2)
        current_mileage = 30000
        last_service_mileage = 0
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_calliope_battery_true_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 2)
        current_mileage = 25000
        last_service_mileage = 0
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_calliope_battery_false_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 1)
        current_mileage = 30000
        last_service_mileage = 0
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
    
    def test_calliope_battery_false_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 1)
        current_mileage = 25000
        last_service_mileage = 0
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
        
        
    def test_glissade_battery_true_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 2)
        current_mileage = 60000
        last_service_mileage = 0
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_glissade_battery_true_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 2)
        current_mileage = 55000
        last_service_mileage = 0
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
    
    def test_glissade_battery_false_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 1)
        current_mileage = 60000
        last_service_mileage = 0
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
    
    def test_glissade_battery_false_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 1)
        current_mileage = 55000
        last_service_mileage = 0
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
        
        
    def test_palindrome_battery_true_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 2)
        warning_light_on = True
        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service())
        

    def test_palindrome_battery_true_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 2)
        warning_light_on = False
        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service())
        
        
    def test_palindrome_battery_false_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 1)
        warning_light_on = True
        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service())
        
        
    def test_palindrome_battery_false_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 1)
        warning_light_on = False
        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertFalse(car.needs_service())
        
        
    def test_rorschach_battery_true_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 4)
        current_mileage = 60000
        last_service_mileage = 0
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_rorschach_battery_true_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 4)
        current_mileage = 55000
        last_service_mileage = 0
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_rorschach_battery_false_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 3)
        current_mileage = 60000
        last_service_mileage = 0
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_rorschach_battery_false_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 3)
        current_mileage = 55000
        last_service_mileage = 0
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
        
        
    def test_thovex_battery_true_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 4)
        current_mileage = 30000
        last_service_mileage = 0
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_thovex_battery_true_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 4)
        current_mileage = 25000
        last_service_mileage = 0
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_thovex_battery_false_engine_true(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 3)
        current_mileage = 30000
        last_service_mileage = 0
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
        
        
    def test_thovex_battery_false_engine_false(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days=365 * 3)
        current_mileage = 25000
        last_service_mileage = 0
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
        
        
        
if __name__ == '__main__':
    unittest.main()
