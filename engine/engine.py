from abc import ABC, abstractmethod
from car import Car


class Engine(Car, ABC):

    def __init__(self, last_service_date, warning_light_is_on, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @abstractmethod
    def needs_service(self):
        pass
