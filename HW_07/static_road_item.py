from road_item import RoadItem


class StaticRoadItem(RoadItem):
    def __init__(self):
        super().__init__()

class StopSign(StaticRoadItem):
    pass

class Intersection(StaticRoadItem):
    pass

class SpeedLimit(StaticRoadItem):
    def __init__(self):
        super().__init__()
        self.speedLimit = 45

    def GetSpeedLimit(self):
        print(f"Speed Limit:{self.speedLimit}")
        return self.speedLimit

class Yield(StaticRoadItem):
    pass
