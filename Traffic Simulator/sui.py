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