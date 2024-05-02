from road_item import RoadItem

class StaticRoadItem(RoadItem):
    pass

class StopSign(StaticRoadItem):
    pass

class Intersection(StaticRoadItem):
    pass

class SpeedLimit(StaticRoadItem):
    def __init__(self, speed_limit=45):
        super().__init__()
        self.speed_limit = speed_limit

    def print_road_item(self, obj):
        return str(self.speed_limit)

class Yield(StaticRoadItem):
    pass
