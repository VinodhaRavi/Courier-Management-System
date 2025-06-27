from service.courier_admin_service import ICourierAdminService
from service.courier_user_service_impl import CourierUserServiceImpl
class CourierAdminServiceImpl(CourierUserServiceImpl, ICourierAdminService):
    def add_courier_staff(self, employee_obj):
        self.company.add_employee(employee_obj)
        return employee_obj._Employee__employee_id
