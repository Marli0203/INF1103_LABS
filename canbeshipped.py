from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    # Create the abstract method to force classes that interface this
    # to implement this abstract method using their own implementation
    @abstractmethod
    def calculate_shipping_cost(self):
        pass