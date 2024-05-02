from enum import Enum
from dynamic_road_item import DynamicRoadItem

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
        self.road_items = []

    def get_x_location(self):
        return self.locx

    def get_y_location(self):
        return self.locy

    def get_length(self):
        return self.length

    def get_heading(self):
        return self.heading

    def add_road_item(self, road_item):
        self.road_items.append(road_item)

    def print(self, pd, obj):
        pd.print_road(self, obj)

        for item in self.road_items:
            item.print_road_item(obj)
