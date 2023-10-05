from abc import ABC

from engine import Engine


class WilloughbyEngine(Engine, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        super().__init__(current_mileage)
        super().__init__(last_service_mileage)

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
