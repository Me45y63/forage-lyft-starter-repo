from .tire import Tire


class CarriganTire(Tire):
    def __init__(self, worn_out):
        self.worn_out = worn_out

    def searchArray(self):
        for i in self.worn_out:
            if i >= 0.9:
                return True
            

    def tire_should_be_serviced(self):
        if self.searchArray():
            return True
        else:
            return False
