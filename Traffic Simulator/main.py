import os
import platform
import time
from map import Map
from gui import MetricGUI
from traffic import TrafficLight
from dynamic_road_item import TrafficLight as TL
from sui import *

@staticmethod
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    sim_input = MetricGUI()
    map_obj = Map()
    cp = ConsolePrint()

    uptown = sim_input.create_road("Uptown", 0, -0.09, 0.180, Heading.North)
    map_obj.add_road(uptown)

    traffic_light1 = TrafficLight(mile_marker=26, red_duration=5, yellow_duration=1, green_duration=3)
    traffic_light2 = TrafficLight(mile_marker=26, green_duration=5, yellow_duration=2, red_duration=3)
    uptown.add_road_item(traffic_light1)
    uptown.add_road_item(traffic_light2)
    traffic_lights = [traffic_light1, traffic_light2]
    
    for time_step in range(30):
        for tl in traffic_lights:
            tl.update()

        cm = CharMatrix()

        map_obj.print(cp, cm)

        for row in cm.map:
            print(''.join(row))

        time.sleep(1)
        clear_screen()

if __name__ == "__main__":
    main()
