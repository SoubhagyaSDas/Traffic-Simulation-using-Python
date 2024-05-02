from traffic import *
from sui import *
import os
import platform

class Simulation:
    def __init__(self):
        self.gui = None
        self.traffic_lights = []
        self.vehicles = []
        self.timer = None

    def update(self):
        for item in self.traffic_lights:
            item.update()

        for vehicle in self.vehicles:
            vehicle.update(1)

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
