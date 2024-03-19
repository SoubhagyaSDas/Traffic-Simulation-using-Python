class ISimOutput:
    def get_speed(self, vehicle):
        pass

class ImperialOutput(ISimOutput):
    def get_speed(self, vehicle):
        return vehicle.getCurrentSpeed()

class MetricOutput(ISimOutput):
    def get_speed(self, vehicle):
        return vehicle.getCurrentSpeed() * 1.6
