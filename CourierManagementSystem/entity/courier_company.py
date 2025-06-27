class CourierCompany:
    def __init__(self, company_name=""):
        self.__company_name = company_name
        self.__courier_details  = []   
        self.__employee_details = []
        self.__location_details = []
    def add_courier(self, c):  self.__courier_details.append(c)
    def add_employee(self, e): self.__employee_details.append(e)
    def add_location(self, l): self.__location_details.append(l)
    def _couriers(self):  return self.__courier_details
    def _employees(self): return self.__employee_details
