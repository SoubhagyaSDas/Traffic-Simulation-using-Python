from  dynamic_road_item import *
from constants import Constants
from abc import ABC, abstractmethod


class Vehicle(DynamicRoadItem):
    def __init__(self):
        super().__init__()
        self.current_speed = 0
        self.desired_speed = 0
        self.speedLimit = 0
        self.color = None 
        self.currentDirection = 0
        self.currentLocation = (0, 0)
        

    def get_current_speed(self):
        return self.current_speed


    def set_desired_speed(self, mph):
        self.desired_speed = mph

    
    def set_current_speed(self, speed):
        if self.current_speed <= speed:  # accelerating
            if speed > self.desired_speed:
                self.current_speed = self.desired_speed
            else:
                self.current_speed = speed
        else:  # braking
            if speed < self.desired_speed:
                self.current_speed = self.desired_speed
            else:
                self.current_speed = speed

    
    def update_speed(self, seconds):
        if self.current_speed > self.desired_speed:
            self.decelerate(seconds)
        elif self.current_speed < self.desired_speed:
            self.accelerate(seconds)
      
    @abstractmethod
    def accelerate(self, seconds_delta):
        pass


    @abstractmethod
    def decelerate(self, seconds_delta):
        pass


    def Turn(self, direction, degrees):
        #print(f"Turning {direction} {degrees}°") # for debugging purposes
        pass


class Car(Vehicle):
    def __init__(self):
        super().__init__() #The super() function is used to give access to methods and properties of a parent or sibling class.

    def accelerate(self, seconds_delta):
        # Acceleration now directly uses m/s without conversion
        self.set_current_speed(self.get_current_speed() + Constants.AccRate * seconds_delta)

    def decelerate(self, seconds_delta):
        # Deceleration now directly uses m/s without conversion
        self.set_current_speed(self.get_current_speed() - Constants.DecRate * seconds_delta)


class Truck(Vehicle):
    def __init__(self,weight):
        super().__init__()
        self.loadWeight = weight

    def SetLoadWeight(self, weight):
        #print(f"Setting Truck load to {weight} lbs.") # for debugging purposes
        pass

    def accelerate(self, seconds_delta):
        # Accelerate based on load weight without conversion
        acc_rate = Constants.AccRateEmpty if self.loadWeight <= 5 else Constants.AccRateFull
        self.set_current_speed(self.get_current_speed() + acc_rate * seconds_delta)

    def decelerate(self, seconds_delta):
        # Decelerate based on load weight without conversion
        dec_rate = Constants.DecRateEmpty if self.loadWeight <= 5 else Constants.DecRateFull
        self.set_current_speed(self.get_current_speed() - dec_rate * seconds_delta)
# from abc import ABC, abstractmethod
# from constants import Constants

# class Vehicle(ABC):
#     def __init__(self):
#         self.currentSpeed = 0.0
#         self.desiredSpeed = 0.0

#     @abstractmethod
#     def accelerate(self, secondsDelta):
#         pass

#     @abstractmethod
#     def decelerate(self, secondsDelta):
#         pass

#     def updateSpeed(self, seconds):
#         if self.currentSpeed < self.desiredSpeed:
#             self.accelerate(seconds)
#         elif self.currentSpeed > self.desiredSpeed:
#             self.decelerate(seconds)
#         # Ensure speed does not go below 0
#         self.currentSpeed = max(0, self.currentSpeed)

#     def setDesiredSpeed(self, mph):
#         self.desiredSpeed = mph

#     def setCurrentSpeed(self, speed):
#         self.currentSpeed = speed

# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()

#     def accelerate(self, secondsDelta):
#         self.setCurrentSpeed(self.currentSpeed + Constants.AccRate * secondsDelta * Constants.MpsToMph)

#     def decelerate(self, secondsDelta):
#         self.setCurrentSpeed(self.currentSpeed - Constants.DecRate * secondsDelta * Constants.MpsToMph)

#     def getCurrentSpeed(self):
#         return self.currentSpeed

# class Truck(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.loadWeight = 0.0

#     def accelerate(self, secondsDelta):
#         if self.loadWeight <= 5:
#             self.setCurrentSpeed(self.currentSpeed + Constants.AccRateEmpty * secondsDelta * Constants.MpsToMph)
#         else:
#             self.setCurrentSpeed(self.currentSpeed + Constants.AccRateFull * secondsDelta * Constants.MpsToMph)

#     def decelerate(self, secondsDelta):
#         if self.loadWeight <= 5:
#             self.setCurrentSpeed(self.currentSpeed - Constants.DecRateEmpty * secondsDelta * Constants.MpsToMph)
#         else:
#             self.setCurrentSpeed(self.currentSpeed - Constants.DecRateFull * secondsDelta * Constants.MpsToMph)

#     def setLoadWeight(self, weight):
#         self.loadWeight = weight

#     def getCurrentSpeed(self):
#         return self.currentSpeed