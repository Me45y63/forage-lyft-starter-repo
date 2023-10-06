from .tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, worn_out):
        self.worn_out = worn_out

    def tire_should_be_serviced(self):
        return sum(self.worn_out) >= 3.0
