# modified using professor's code
from abc import ABC, abstractmethod
from Constants import Constants
from dynamic_road_item import Vehicle
from road import Road
from sim_output import *


class GUI(ISimInput, ISimOutput, ABC):
    @abstractmethod
    def get_speed(self, vehicle: Vehicle) -> float:
        pass

    @abstractmethod
    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        pass

    @abstractmethod
    def create_road(self, name, locx, locy, len, hdg):
        pass

class MetricGUI(GUI):
    def get_speed(self, vehicle: Vehicle) -> float:
        # return vehicle.get_current_speed() * Constants.MpsToKph
        speed_kmh = vehicle.get_current_speed() * Constants.MpsToKph
        return f"{speed_kmh:.2f} Km/h"

    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        vehicle.set_desired_speed(speed / Constants.MpsToKph)

    def create_road(self, name, locx, locy, len, hdg):
        # Implementation based on Metric system from C# MetricGUI
        return Road(name, locx / Constants.MetersToKm, locy / Constants.MetersToKm, len / Constants.MetersToKm, hdg)

class ImperialGUI(GUI):
    def get_speed(self, vehicle: Vehicle) -> float:
        # return vehicle.get_current_speed() * Constants.MpsToMph
        speed_mph = vehicle.get_current_speed() * Constants.MpsToMph
        return f"{speed_mph:.2f} mph"

    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        vehicle.set_desired_speed(speed / Constants.MpsToMph)

    def create_road(self, name, locx, locy, len, hdg):
        # Implementation based on Imperial system from C# ImperialGUI
        return Road(name, locx / Constants.MetersToMiles, locy / Constants.MetersToMiles, len / Constants.MetersToMiles, hdg)

