import unittest
import sys
sys.path.append("C:\\Programming\\forage-lyft-starter-repo-1\\src")

from car.tire.carrigan_tire import CarriganTire


class CarriganTireTest(unittest.TestCase):
    
    
    def test_carrigan_tire_false(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())
        
    
    def test_carrigan_tire_true(self):
        tire_wear = [0.1, 0.1, 0.1, 0.9]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())


if __name__ == '__main__':
    unittest.main()