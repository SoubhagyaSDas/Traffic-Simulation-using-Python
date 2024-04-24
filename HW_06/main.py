import os
import platform
import time
from map import *
from gui import *
from simulation import *
from vehicle import Car, Truck
from static_road_item import *
from Constants import *
from sim_output import *
from sui import *
from traffic import *

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
    traffic_light2.current_color = 'green'
    traffic_lights = [traffic_light1, traffic_light2]

    for time_step in range(30):
        for tl in traffic_lights:
            tl.update()

        cm = CharMatrix()

        TrafficLight.print_traffic_lights(traffic_lights, cm)  

        map_obj.print(cp, cm)

        for row in cm.map:
            print(''.join(row))

        time.sleep(1)
        clear_screen()

if __name__ == "__main__":
    main()
    
#     # User input for choosing the system
#     system_choice = input("Choose the system (M for Metric, I for Imperial): ").upper()
#     if system_choice == 'M':
#         gui = MetricGUI()
#     else:
#         gui = ImperialGUI()
    
#     # User input for speed limit...
#     speed_limit = float(input("Enter the speed limit: "))
    
#     # Initialize vehicles and set their desired speed using the GUI
#     car = Car()
#     gui.set_speed_limit(car, speed_limit)
#     truck1 = Truck(4)
#     gui.set_speed_limit(truck1, speed_limit)
#     truck2 = Truck(8)
#     gui.set_speed_limit(truck2, speed_limit)

#     vehicles = [car, truck1, truck2]

#     # Simulation loop
#     for _ in range(11):
#         for v in vehicles:
#             v.update_speed(1)
#             print(f"{v.__class__.__name__} speed: {gui.get_speed(v)}")

# if __name__ == "__main__":
#     main()
# from vehicle import Car, Truck
# from constants import Constants
# from sim_output import MetricOutput

# def main():
#     car = Car()
#     car.setDesiredSpeed(65.0)
#     truck1 = Truck()
#     truck1.setLoadWeight(4)
#     truck1.setDesiredSpeed(55.0)
#     truck2 = Truck()
#     truck2.setLoadWeight(8)
#     truck2.setDesiredSpeed(50.0)
#     vehicles = [car, truck1, truck2]

#     sim_output = MetricOutput()

#     for i in range(11):
#         for v in vehicles:
#             v.updateSpeed(1) # Pass the time elapsed as an argument
#             speed = sim_output.get_speed(v)
#             unit = "km/h" if isinstance(sim_output, MetricOutput) else "mph"
#             print(f"HW3_2024_OOP.{type(v).__name__} speed: {speed:.2f} {unit}")

# if __name__ == "__main__":
#     main()