from .tire import Tire


class CarriganTire(Tire):
    def __init__(self, worn_out):
        self.worn_out = worn_out       
            
    def tire_should_be_serviced(self):
        for i in self.worn_out:
            if i >= 0.9:
                return True
