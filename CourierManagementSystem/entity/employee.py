class Employee:
    def __init__(self, employee_id=None, employee_name="", email="",
                contact_number="", role="", salary=0.0):
        self.__employee_id = employee_id
        self.__employee_name = employee_name
        self.__email = email
        self.__contact_number = contact_number
        self.__role = role
        self.__salary = salary
    def __str__(self):
        return f"Emp[{self.__employee_id}] {self.__employee_name}"
