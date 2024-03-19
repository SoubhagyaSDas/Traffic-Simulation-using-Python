class Simulation:
    def __init__(self):
        self.gui = None
        self.traffic_lights = []
        self.vehicles = []
        self.timer = None
        # 1 to many relationship with TrafficLight, Vehicle, and Timer
