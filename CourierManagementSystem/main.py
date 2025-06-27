from entity.courier_company import CourierCompany
from entity.courier import Courier
from service.courier_user_service_impl import CourierUserServiceImpl

company = CourierCompany("FastShip")
user_service = CourierUserServiceImpl(company)

def menu():
    print("\n1 Place order\n2 Track order\n3 Exit")
    return input("Choice: ")

while True:
    choice = menu()
    if choice == "1":
        sender = input("Sender name: ")
        receiver = input("Receiver name: ")
        c = Courier(courier_id=len(company._couriers())+1,
                    sender_name=sender,
                    sender_address="Src",
                    receiver_name=receiver,
                    receiver_address="Dest",
                    weight=1.0)
        print("Tracking #:", user_service.place_order(c))
    elif choice == "2":
        tn = input("Enter tracking #: ")
        try:
            print("Status:", user_service.get_order_status(tn))
        except Exception as e:
            print(e)
    else:
        break



#python main.py
