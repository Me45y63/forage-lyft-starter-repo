from .tire import Tire


class CarriganTire(Tire):
    def __init__(self, worn_out):
        self.worn_out = worn_out

    def searchArray(self):
        if 0.9 in self.worn_out:
            return True
        else:
            return False

    def tire_should_be_serviced(self):
        if self.searchArray():
            return True
        else:
            return False
