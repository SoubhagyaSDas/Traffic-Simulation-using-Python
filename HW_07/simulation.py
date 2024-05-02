class Simulation:
    def __init__(self):
        self.dynamic_road_items = []

    def add_dynamic_road_item(self, item):
        self.dynamic_road_items.append(item)

    def update(self):
        for item in self.dynamic_road_items:
            item.update()
