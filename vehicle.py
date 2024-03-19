from constants import Constants

class Vehicle:
    def __init__(self):
        self.currentSpeed = 0.0
        self.currentDirection = 0.0
        self.currentLocation = (0.0, 0.0)
        self.desiredSpeed = 0.0

    def accelerate(self, secondsDelta):
        pass

    def decelerate(self, secondsDelta):
        pass

    def updateSpeed(self, seconds):
        if self.currentSpeed < self.desiredSpeed:
            self.accelerate(seconds)
        elif self.currentSpeed > self.desiredSpeed:
            self.decelerate(seconds)

    def setDesiredSpeed(self, mph):
        self.desiredSpeed = mph

    def setCurrentSpeed(self, speed):
        self.currentSpeed = speed

    def turn(self, direction, degrees):
        pass

class Car(Vehicle):
    def accelerate(self, secondsDelta):
        self.setCurrentSpeed(self.currentSpeed + Constants.AccRate * secondsDelta)

    def decelerate(self, secondsDelta):
        self.setCurrentSpeed(self.currentSpeed - Constants.DecRate * secondsDelta)

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.loadWeight = 0.0

    def accelerate(self, secondsDelta):
        if self.loadWeight <= 5:
            self.setCurrentSpeed(self.currentSpeed + Constants.AccRateEmpty * secondsDelta)
        else:
            self.setCurrentSpeed(self.currentSpeed + Constants.AccRateFull * secondsDelta)

    def decelerate(self, secondsDelta):
        if self.loadWeight <= 5:
            self.setCurrentSpeed(self.currentSpeed - Constants.DecRateEmpty * secondsDelta)
        else:
            self.setCurrentSpeed(self.currentSpeed - Constants.DecRateFull * secondsDelta)

    def setLoadWeight(self, weight):
        self.loadWeight = weight
