from abc import ABC, abstractmethod
from constants import Constants

class Vehicle(ABC):
    def __init__(self):
        self.currentSpeed = 0.0
        self.desiredSpeed = 0.0

    @abstractmethod
    def accelerate(self, secondsDelta):
        pass

    @abstractmethod
    def decelerate(self, secondsDelta):
        pass

    def updateSpeed(self, seconds):
        if self.currentSpeed < self.desiredSpeed:
            self.accelerate(seconds)
        elif self.currentSpeed > self.desiredSpeed:
            self.decelerate(seconds)
        # Ensure speed does not go below 0
        self.currentSpeed = max(0, self.currentSpeed)

    def setDesiredSpeed(self, mph):
        self.desiredSpeed = mph

    def setCurrentSpeed(self, speed):
        self.currentSpeed = speed

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def accelerate(self, secondsDelta):
        self.setCurrentSpeed(self.currentSpeed + Constants.AccRate * secondsDelta * Constants.MpsToMph)

    def decelerate(self, secondsDelta):
        self.setCurrentSpeed(self.currentSpeed - Constants.DecRate * secondsDelta * Constants.MpsToMph)

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.loadWeight = 0.0

    def accelerate(self, secondsDelta):
        if self.loadWeight <= 5:
            self.setCurrentSpeed(self.currentSpeed + Constants.AccRateEmpty * secondsDelta * Constants.MpsToMph)
        else:
            self.setCurrentSpeed(self.currentSpeed + Constants.AccRateFull * secondsDelta * Constants.MpsToMph)

    def decelerate(self, secondsDelta):
        if self.loadWeight <= 5:
            self.setCurrentSpeed(self.currentSpeed - Constants.DecRateEmpty * secondsDelta * Constants.MpsToMph)
        else:
            self.setCurrentSpeed(self.currentSpeed - Constants.DecRateFull * secondsDelta * Constants.MpsToMph)

    def setLoadWeight(self, weight):
        self.loadWeight = weight
