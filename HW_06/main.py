from map import *
from gui import *
from simulation import *
from vehicle import Car, Truck
from static_road_item import SpeedLimit
from Constants import Constants
from sim_output import *
from sui import *

def main():
    simInput = MetricGUI()
    Uptown = simInput.create_road("Uptown", 0.0, -0.09, .180, Heading.North)
    Crosstown = simInput.create_road("Crosstown", -0.09, 0.0, .180, Heading.East)

    # Corrected instantiation of CharMatrix
    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Map()
    map_obj.add_road(Uptown)
    map_obj.add_road(Crosstown)
    cp = ConsolePrint()
    map_obj.print(cp, cm)

    for i in range(Constants.CharMapSize):
        print("".join(cm.map[i]))
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