from abc import ABC
from engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        super().__init__(warning_light_is_on)


    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
