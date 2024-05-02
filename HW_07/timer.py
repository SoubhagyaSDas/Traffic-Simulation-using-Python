import os
import platform
import time
from simulation import Simulation
from map import Map
from gui import MetricGUI
from traffic import TrafficLight
from vehicle import Car
from road import Road, Heading
from constants import Constants
from sim_output import ConsolePrint

class Timer:
    @staticmethod
    def clear_screen():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def start_simulation():
        map_obj = Map()
        cp = ConsolePrint()

        uptown = Road("Uptown", 0, -0.09, 0.180, Heading.North)
        map_obj.add_road(uptown)

        car = Car()
        uptown.add_vehicle(car)

        traffic_light1 = TrafficLight(mile_marker=26, red_duration=5, yellow_duration=1, green_duration=3)
        traffic_light2 = TrafficLight(mile_marker=52, green_duration=5, yellow_duration=2, red_duration=3)
        traffic_lights = [traffic_light1, traffic_light2]

        sim = Simulation()
        for tl in traffic_lights:
            sim.add_dynamic_road_item(tl)

        for time_step in range(30):
            sim.update()

            cm = CharMatrix()

            for tl in traffic_lights:
                tl.print(cp, cm)

            map_obj.print(cp, cm)

            for row in cm.map:
                print(''.join(row))

            time.sleep(1)
            Timer.clear_screen()

if __name__ == "__main__":
    Timer.start_simulation()
