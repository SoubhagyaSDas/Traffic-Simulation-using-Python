class Map:
    def __init__(self):
        self.roads = []

    def add_road(self, road):
        self.roads.append(road)

    def print(self, print_driver, obj):
        for road in self.roads:
            road.print(print_driver, obj)