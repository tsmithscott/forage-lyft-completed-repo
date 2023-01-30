from abc import abstractmethod

from serviceable import Serviceable


class Battery(Serviceable):

    @abstractmethod
    def needs_service(self):
        pass
