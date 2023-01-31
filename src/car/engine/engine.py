from abc import abstractmethod

from car.utils.serviceable import Serviceable


class Engine(Serviceable):

    @abstractmethod
    def needs_service(self):
        pass
        