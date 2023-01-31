from car.utils.serviceable import Serviceable
from car.battery.battery import Battery
from car.engine.engine import Engine


class Car(Serviceable):
    
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
        
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()