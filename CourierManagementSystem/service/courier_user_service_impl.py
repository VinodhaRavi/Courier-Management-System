from service.courier_user_service import ICourierUserService
from exception.tracking_number_not_found import TrackingNumberNotFoundException

class CourierUserServiceImpl(ICourierUserService):
    def __init__(self, company_obj):
        self.company = company_obj

    def place_order(self, courier_obj):
        self.company.add_courier(courier_obj)
        return courier_obj.get_tracking_number()

    def get_order_status(self, tracking_number):
        for c in self.company._couriers():
            if c.get_tracking_number() == tracking_number:
                return c.get_status()
        raise TrackingNumberNotFoundException("Tracking number not found")

    def cancel_order(self, tracking_number):
        for c in self.company._couriers():
            if c.get_tracking_number() == tracking_number:
                c.set_status("Cancelled")
                return True
        return False

    def get_assigned_order(self, courier_staff_id):
        return self.company._couriers()   
