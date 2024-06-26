from dynamic_road_item import RoadItem

class TrafficLight(RoadItem):
    def __init__(self, mile_marker, red_duration, yellow_duration, green_duration, start_color='red'):
        super().__init__(mile_marker)
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.current_color = start_color
        self.timer = 0  
        
    def update(self, seconds=1):
        self.timer += seconds
        cycle_duration = self.red_duration + self.yellow_duration + self.green_duration
        self.timer %= cycle_duration
        if self.timer <= self.red_duration:
            self.current_color = 'red'
        elif self.timer <= self.red_duration + self.yellow_duration:
            self.current_color = 'yellow'
        else:
            self.current_color = 'green'

    def print(self, print_driver, obj):
        print_driver.print_traffic_light(self, obj)
