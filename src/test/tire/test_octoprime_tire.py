import unittest
import sys
sys.path.append("C:\\Programming\\forage-lyft-starter-repo-1\\src")

from car.tire.octoprime_tire import OctoprimeTire


class OctoprimeTireTest(unittest.TestCase):
    
    
    def test_octoprime_tire_false(self):
        tire_wear = [0.1, 0.1, 0.1, 0.1]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())
        
    
    def test_octoprime_tire_true(self):
        tire_wear = [1, 1, 1, 1]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())


if __name__ == '__main__':
    unittest.main()