from abc import ABC, abstractmethod
class ICourierUserService(ABC):
    @abstractmethod
    def place_order(self, courier_obj): ...
    @abstractmethod
    def get_order_status(self, tracking_number): ...
    @abstractmethod
    def cancel_order(self, tracking_number): ...
    @abstractmethod
    def get_assigned_order(self, courier_staff_id): ...
