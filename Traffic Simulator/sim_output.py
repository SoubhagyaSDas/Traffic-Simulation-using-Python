from abc import ABC, abstractmethod
from Constants import Constants
from vehicle import Vehicle  # If the Vehicle class is needed for type annotations

class ISimOutput(ABC):
    @abstractmethod
    def get_speed(self, vehicle: Vehicle) -> float:
        pass

class ISimInput(ABC):
    @abstractmethod
    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        pass

