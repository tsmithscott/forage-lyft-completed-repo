from car.tire.tire import Tire


class CarriganTire(Tire):

    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tire_wear)
