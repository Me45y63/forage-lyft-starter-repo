from .tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, worn_out):
        self.worn_out = worn_out

    def calcTotal(self) -> int:
        result = 0
        for i in self.worn_out:
            result += i
        return result

    def tire_should_be_serviced(self):
        if self.calcTotal() >= 3:
            return True
        else:
            return False
