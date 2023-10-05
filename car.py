from abc import ABC, abstractmethod


class CarFactory:

    def create_car(self, current_date, last_service_date, current_mileage, last_service_mileage):
        """Create cars"""


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
