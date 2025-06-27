class Location:
    def __init__(self, location_id=None, location_name="", address=""):
        self.__location_id = location_id
        self.__location_name = location_name
        self.__address = address
    def __str__(self):
        return f"Loc[{self.__location_id}] {self.__location_name}"
