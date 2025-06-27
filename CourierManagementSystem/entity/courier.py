import datetime
class Courier:
    __track_seed = 10000               # static tracking generator
    def __init__(self, courier_id=None, sender_name="", sender_address="",
                receiver_name="", receiver_address="", weight=0.0,
                status="YetToDispatch", delivery_date=None, user_id=None):
        self.__courier_id = courier_id
        self.__sender_name = sender_name
        self.__sender_address = sender_address
        self.__receiver_name = receiver_name
        self.__receiver_address = receiver_address
        self.__weight = weight
        self.__status = status
        self.__tracking_number = f"TRK{Courier.__track_seed}"
        Courier.__track_seed += 1
        self.__delivery_date = delivery_date or datetime.date.today()
        self.__user_id = user_id

    def get_tracking_number(self): return self.__tracking_number
    def get_status(self):          return self.__status
    def set_status(self, s):       self.__status = s
    def __str__(self):
        return f"Courier[{self.__courier_id}] {self.__tracking_number}"
