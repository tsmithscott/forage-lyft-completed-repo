from abc import abstractmethod

from car.utils.serviceable import Serviceable


class Battery(Serviceable):

    @abstractmethod
    def needs_service(self):
        pass
