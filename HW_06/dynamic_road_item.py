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
