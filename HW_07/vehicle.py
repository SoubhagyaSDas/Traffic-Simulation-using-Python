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


