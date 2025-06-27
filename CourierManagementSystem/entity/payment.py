import datetime
class Payment:
    def __init__(self, payment_id=None, courier_id=None,
                amount=0.0, payment_date=None):
        self.__payment_id = payment_id
        self.__courier_id = courier_id
        self.__amount = amount
        self.__payment_date = payment_date or datetime.date.today()
    def __str__(self):
        return f"Pay[{self.__payment_id}] ₹{self.__amount}"
