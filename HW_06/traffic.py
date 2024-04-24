from dynamic_road_item import *

class TrafficLight(DynamicRoadItem):
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

    @staticmethod
    def print_traffic_lights(traffic_lights, char_matrix):
        first_tl_row_index = len(char_matrix.map) - 13
        second_tl_row_index = first_tl_row_index - 13
        symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}[traffic_lights[0].current_color]
        char_matrix.map[first_tl_row_index][traffic_lights[0].mile_marker] = symbol
        symbol = {'green': 'O', 'red': 'X', 'yellow': '-'}[traffic_lights[1].current_color]
        char_matrix.map[second_tl_row_index][traffic_lights[1].mile_marker] = symbol