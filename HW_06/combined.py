# main.py
import os
import platform
import time
from map import *
from gui import *
from simulation import *
from vehicle import Car, Truck
from static_road_item import *
from Constants import *
from sim_output import *
from sui import *
from traffic import *

@staticmethod
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    sim_input = MetricGUI()
    map_obj = Map()
    cp = ConsolePrint()

    uptown = sim_input.create_road("Uptown", 0, -0.09, 0.180, Heading.North)
    map_obj.add_road(uptown)

    traffic_light1 = TrafficLight(mile_marker=26, red_duration=5, yellow_duration=1, green_duration=3)
    traffic_light2 = TrafficLight(mile_marker=26, green_duration=5, yellow_duration=2, red_duration=3)
    traffic_light2.current_color = 'green'
    traffic_lights = [traffic_light1, traffic_light2]

    for time_step in range(30):
        for tl in traffic_lights:
            tl.update()

        cm = CharMatrix()

        TrafficLight.print_traffic_lights(traffic_lights, cm)  

        map_obj.print(cp, cm)

        for row in cm.map:
            print(''.join(row))

        time.sleep(1)
        clear_screen()

if __name__ == "__main__":
    main()

#dynamic_road_item.py
from abc import ABC, abstractmethod
from road_item import RoadItem


class DynamicRoadItem(RoadItem, ABC):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)

    @abstractmethod
    def update(self, seconds: int):
        pass

class TrafficLight(DynamicRoadItem):
    pass

class Vehicle(DynamicRoadItem):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

# gui.py
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
        speed_kmh = vehicle.get_current_speed() * Constants.MpsToKph
        return f"{speed_kmh:.2f} Km/h"

    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        vehicle.set_desired_speed(speed / Constants.MpsToKph)

    def create_road(self, name, locx, locy, len, hdg):
        return Road(name, locx / Constants.MetersToKm, locy / Constants.MetersToKm, len / Constants.MetersToKm, hdg)

class ImperialGUI(GUI):
    def get_speed(self, vehicle: Vehicle) -> float:
        speed_mph = vehicle.get_current_speed() * Constants.MpsToMph
        return f"{speed_mph:.2f} mph"

    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        vehicle.set_desired_speed(speed / Constants.MpsToMph)

    def create_road(self, name, locx, locy, len, hdg):
        return Road(name, locx / Constants.MetersToMiles, locy / Constants.MetersToMiles, len / Constants.MetersToMiles, hdg)
    
#map.py
class Map:
    def __init__(self):
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def print(self, print_driver, obj):
        for road in self.roads:
            road.print(print_driver, obj)

#road_item.py
class RoadItem:
    def __init__(self, mile_marker, current_road=None):
        self.mile_marker = mile_marker
        self.current_road = current_road
        self.next_item = None
        self.prev_item = None

    def get_mile_marker(self):
        return self.mile_marker

    def get_current_road(self):
        return self.current_road

    def set_current_road(self, road):
        self.current_road = road

    def get_next(self):
        return self.next_item

    def set_next(self, next_item):
        self.next_item = next_item

    def get_previous(self):
        return self.prev_item

    def set_previous(self, prev_item):
        self.prev_item = prev_item

#road.py
from enum import Enum

class Heading(Enum):
    North = 0
    South = 1
    East = 2
    West = 3

class Road:
    def __init__(self, name, locx, locy, length, heading):
        self.name = name
        self.locx = locx
        self.locy = locy
        self.length = length
        self.heading = heading

    def get_x_location(self):
        return self.locx

    def get_y_location(self):
        return self.locy

    def get_length(self):
        return self.length

    def get_heading(self):
        return self.heading

    def print(self, pd, o):
        pd.print_road(self, o)

#sui.py
from abc import ABC, abstractmethod
import numpy as np

from common import Conversions
from Constants import Constants
from road import Heading  

class CharMatrix:
    def __init__(self, size=Constants.CharMapSize):
        self.size = size
        self.map = [[' ' for _ in range(size)] for _ in range(size)]
    def clear(self):
            
            self.map = [[' ' for _ in range(self.size)] for _ in range(self.size)]

class IPrintDriver(ABC):
    @abstractmethod
    def print_road(self, road, obj):
        pass

    @abstractmethod
    def print_car(self, car, obj):
        pass

class ConsolePrint(IPrintDriver):
    def print_road(self, road, obj):
        cm = obj
        CCx = Conversions.wc_point_to_cc_point(road.get_x_location())
        CCy = Conversions.wc_point_to_cc_point(-road.get_y_location())
        distance = 0
        CCRoadLength = Conversions.wc_length_to_cc_length(road.get_length())

        if road.get_heading() == Heading.North:
            x = int(CCx)
            if 0 <= x < Constants.CharMapSize:
                while distance < CCRoadLength:
                    y = int(CCy - distance)
                    if 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = '|'
                        cm.map[y][x + 2] = '|'
                        cm.map[y][x + 4] = '|'
                    distance += 1
        elif road.get_heading() == Heading.East:
            y = int(CCy)
            if 0 <= y < Constants.CharMapSize:
                while distance < CCRoadLength:
                    x = int(CCx + distance)
                    if 0 <= x < Constants.CharMapSize:
                        cm.map[y][x] = '-'
                        cm.map[y + 2][x] = '-'
                        cm.map[y + 4][x] = '-'
                    distance += 1
        elif road.get_heading() == Heading.South:
            x = int(CCx)
            if 0 <= x < Constants.CharMapSize:
                while distance < CCRoadLength:
                    y = int(CCy + distance)
                    if 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = '|'
                        cm.map[y][x + 2] = '|'
                        cm.map[y][x + 4] = '|'
                    distance += 1
        elif road.get_heading() == Heading.West:
            y = int(CCy)
            if 0 <= y < Constants.CharMapSize:
                while distance < CCRoadLength:
                    x = int(CCx - distance)
                    if 0 <= x < Constants.CharMapSize:
                        cm.map[y][x] = '-'
                        cm.map[y + 2][x] = '-'
                        cm.map[y + 4][x] = '-'
                    distance += 1

    def print_car(self, car, obj):
        pass  

#traffic.py
from dynamic_road_item import *

class TrafficLight(DynamicRoadItem):
    def __init__(self, mile_marker, red_duration, yellow_duration, green_duration, start_color='red'):
        super().__init__(mile_marker)
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.current_color = start_color
        self.timer = 0  
        
    def update(self, seconds=1):
        self.timer += seconds
        cycle_duration = self.red_duration + self.yellow_duration + self.green_duration
        self.timer %= cycle_duration
        if self.timer <= self.red_duration:
            self.current_color = 'red'
        elif self.timer <= self.red_duration + self.yellow_duration:
            self.current_color = 'yellow'
        else:
            self.current_color = 'green'

    @staticmethod
    def print_traffic_lights(traffic_lights, char_matrix):
        first_tl_row_index = len(char_matrix.map) - 13
        second_tl_row_index = first_tl_row_index - 13
        symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}[traffic_lights[0].current_color]
        char_matrix.map[first_tl_row_index][traffic_lights[0].mile_marker] = symbol
        symbol = {'green': 'O', 'red': 'X', 'yellow': '-'}[traffic_lights[1].current_color]
        char_matrix.map[second_tl_row_index][traffic_lights[1].mile_marker] = symbol

#dynamic_road_item
from abc import ABC, abstractmethod
from road_item import RoadItem


class DynamicRoadItem(RoadItem, ABC):
    def __init__(self, mile_marker, current_road=None):
        super().__init__(mile_marker, current_road)

    @abstractmethod
    def update(self, seconds: int):
        pass

class TrafficLight(DynamicRoadItem):
    pass

class Vehicle(DynamicRoadItem):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass


#vechicle.py
from dynamic_road_item import *
from Constants import Constants
from abc import ABC, abstractmethod

class Vehicle(DynamicRoadItem):
    def __init__(self):
        super().__init__()
        self.current_speed = 0
        self.desired_speed = 0
        self.speed_limit = 0
        self.color = None
        self.current_direction = 0
        self.current_location = (0, 0)

    def get_current_speed(self) -> int:
        return self.current_speed

    def set_desired_speed(self, mph: int):
        self.desired_speed = mph

    def set_current_speed(self, speed: int):
        if self.current_speed <= speed:  # accelerating
            self.current_speed = min(speed, self.desired_speed)
        else:  # braking
            self.current_speed = max(speed, self.desired_speed)

    def update_speed(self, seconds: int):
        if self.current_speed > self.desired_speed:
            self.decelerate(seconds)
        elif self.current_speed < self.desired_speed:
            self.accelerate(seconds)

    @abstractmethod
    def accelerate(self, seconds_delta: int):
        pass

    @abstractmethod
    def decelerate(self, seconds_delta: int):
        pass

    def turn(self, direction: str, degrees: int):
        #print(f"Turning {direction} {degrees}°") # for debugging purposes
        pass

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def accelerate(self, seconds_delta: int):
        # Acceleration now directly uses m/s without conversion
        self.set_current_speed(self.get_current_speed() + Constants.AccRate * seconds_delta)

    def decelerate(self, seconds_delta: int):
        # Deceleration now directly uses m/s without conversion
        self.set_current_speed(self.get_current_speed() - Constants.DecRate * seconds_delta)

class Truck(Vehicle):
    def __init__(self, weight: int):
        super().__init__()
        self.load_weight = weight

    def set_load_weight(self, weight: int):
        #print(f"Setting Truck load to {weight} lbs.") # for debugging purposes
        pass

    def accelerate(self, seconds_delta: int):
        # Accelerate based on load weight without conversion
        acc_rate = Constants.AccRateEmpty if self.load_weight <= 5 else Constants.AccRateFull
        self.set_current_speed(self.get_current_speed() + acc_rate * seconds_delta)

    def decelerate(self, seconds_delta: int):
        # Decelerate based on load weight without conversion
        dec_rate = Constants.DecRateEmpty if self.load_weight <= 5 else Constants.DecRateFull
        self.set_current_speed(self.get_current_speed() - dec_rate * seconds_delta)

#common.py
class Conversions:
    @staticmethod
    def wc_point_to_cc_point(val):
        from Constants import Constants  
        return int(val * (Constants.CharMapSize / Constants.WorldSize) + (Constants.CharMapSize / 2))

    @staticmethod
    def wc_length_to_cc_length(val):
        from Constants import Constants  
        return int(val * (Constants.CharMapSize / Constants.WorldSize))
    
#constants.py
class Constants:
    AccRate = 3.5  # Acceleration rate for cars in m/s
    AccRateEmpty = 2.5  # Acceleration rate for light trucks in m/s
    AccRateFull = 1.0  # Acceleration rate for heavy trucks in m/s
    DecRate = 7.0  # Braking rate for cars in m/s
    DecRateEmpty = 5.0  # Braking rate for light trucks in m/s
    DecRateFull = 2.0  # Braking rate for light trucks in m/s
    MpsToMph = 2.237
    MpsToKph = 3.6
    MetersToMiles = 0.000621371
    MetersToKm = 0.001
    CharMapSize = 40
    WorldSize = 200.0

#simulation.py
class Simulation:
    def __init__(self):
        self.gui = None
        self.traffic_lights = []
        self.vehicles = []
        self.timer = None

#static_road_item.py
from road_item import RoadItem


class StaticRoadItem(RoadItem):
    def __init__(self):
        super().__init__()

class StopSign(StaticRoadItem):
    pass

class Intersection(StaticRoadItem):
    pass

class SpeedLimit(StaticRoadItem):
    def __init__(self):
        super().__init__()
        self.speedLimit = 45

    def GetSpeedLimit(self):
        print(f"Speed Limit:{self.speedLimit}")
        return self.speedLimit

class Yield(StaticRoadItem):
    pass

#sim_output.py
from abc import ABC, abstractmethod
from Constants import Constants
from vehicle import Vehicle  # If the Vehicle class is needed for type annotations

class ISimOutput(ABC):
    @abstractmethod
    def get_speed(self, vehicle: Vehicle) -> float:
        pass

class ISimInput(ABC):
    @abstractmethod
    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        pass

#timer.py
class Timer:
    pass
