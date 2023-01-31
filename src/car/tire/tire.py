from abc import abstractmethod

from car.utils.serviceable import Serviceable


class Tire(Serviceable):

    @abstractmethod
    def needs_service(self):
        pass
