import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    
    def test_battery_needs_service(self):
        last_service_date = datetime(2018, 5, 17)
        current_date = datetime.now()
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_needs_service(self):
        last_service_date = datetime.now()
        current_date = datetime(2020, 5, 17)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    
    def test_battery_needs_service(self):
        last_service_date = datetime(2018, 5, 17)
        current_date = datetime.now()
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_needs_service(self):
        last_service_date = datetime.now()
        current_date = datetime(2020, 5, 17)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
