from vehicle import Car, Truck
from constants import Constants
from sim_output import MetricOutput

def main():
    car = Car()
    car.setDesiredSpeed(65.0)
    truck1 = Truck()
    truck1.setLoadWeight(4)
    truck1.setDesiredSpeed(55.0)
    truck2 = Truck()
    truck2.setLoadWeight(8)
    truck2.setDesiredSpeed(50.0)
    vehicles = [car, truck1, truck2]

    sim_output = MetricOutput()

    for i in range(11):
        for v in vehicles:
            v.updateSpeed(1) # Pass the time elapsed as an argument
            speed = sim_output.get_speed(v)
            unit = "km/h" if isinstance(sim_output, MetricOutput) else "mph"
            print(f"HW3_2024_OOP.{type(v).__name__} speed: {speed:.2f} {unit}")

if __name__ == "__main__":
    main()
