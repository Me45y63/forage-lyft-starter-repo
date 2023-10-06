import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):

    def test_tire_should_be_serviced_true(self):
        worn_out = [0.1, 0.3, 0.5, 0.9]
        tire = CarriganTire(worn_out)
        self.assertTrue(tire.tire_should_be_serviced())

    def test_tire_should_be_serviced_false(self):
        worn_out = [0.1, 0.3, 0.5, 0.7]
        tire = CarriganTire(worn_out)
        self.assertFalse(tire.tire_should_be_serviced())


class TestOctoprimeTire(unittest.TestCase):

    def test_tire_should_be_serviced_true(self):
        worn_out = [0.5, 0.9, 0.9, 0.9]
        tire = OctoprimeTire(worn_out)
        self.assertTrue(tire.tire_should_be_serviced())

    def test_tire_should_be_serviced_false(self):
        worn_out = [0.1, 0.3, 0.5, 0.7]
        tire = OctoprimeTire(worn_out)
        self.assertFalse(tire.tire_should_be_serviced())
