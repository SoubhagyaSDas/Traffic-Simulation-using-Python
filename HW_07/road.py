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
        self.traffic_lights = []

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    def get_x_location(self):
        return self.locx

    def get_y_location(self):
        return self.locy

    def get_length(self):
        return self.length

    def get_heading(self):
        return self.heading

    def print(self, pd, obj):
        pd.print_road(self, obj)
        for tl in self.traffic_lights:
            tl.print(pd, obj)  # Change this line to use TrafficLight's method
