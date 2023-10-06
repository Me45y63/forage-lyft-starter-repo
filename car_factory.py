from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
from car import Car


class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, worn_out) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(worn_out)
        car = Car(engine, battery, tire)
        return car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, worn_out) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(worn_out)
        car = Car(engine, battery, tire)
        return car


    def create_palindrome(self, current_date, last_service_date, warning_light_is_on, worn_out) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(worn_out)
        car = Car(engine, battery, tire)
        return car


    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, worn_out) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(worn_out)
        car = Car(engine, battery, tire)
        return car


    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, worn_out) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(worn_out)
        car = Car(engine, battery, tire)
        return car
