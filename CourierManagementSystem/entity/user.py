class User:
    def __init__(self, user_id=None, user_name="", email="", password="",
                contact_number="", address=""):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__contact_number = contact_number
        self.__address = address
    def get_user_id(self):      
        return self.__user_id
    def set_user_id(self, v):   
        self.__user_id = v
    def __str__(self):
        return f"User[{self.__user_id}] {self.__user_name}"
