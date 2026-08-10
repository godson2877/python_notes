 

# def user():
#     print("Welcome to the Bus Ticket Booking System")
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     id_type = input("Enter your ID type : ")
#     return name, age, id_type

# def check_user(name, age, id_type):
#     if age<18:
#         print(f" {name}, you are not eligible to book a ticket.")
#         return False
#     elif id_type not in ["Aadhar", "Voter ID", "Driving License"]:
#         print(f"{name}, Invalid ID type. Please provide a valid ID.")
#         return False
#     return True

# def check_bus_availability(locations):
#     print(f"stops are{locations}")
#     source=input("enter pick_up point :")
#     destination=input("enter destination :")
#     if source== destination:
#         print ("invalid ")
#     elif source  and destination not in locations:
#         print("invlaid")
#     else:
#         enter_time=input("enter the time for boarding")
#         print(f"your bus is booked from {source} to {destination} at {enter_time}")


# def admin():
#     print("admin portal , used to update ")
#     locations=["kollam","thiruvantapuram"]
#     print (f"loacations are {locations}")
#     choice =0
#     while choice!=4:
#         choice=int(input("enter a choice/n " 
#         "1) press 1 to add locations /n" 
#         "2) press 2 to edit locations /n"
#         "3)press 3 to remove locations /n"
#         "4) press 4 to exit admin/n"))
#         if choice == 1:
#             add = input("enter location :")
#             locations.append(add)
#         if choice == 2:
#             demo=input("enter the location to be changed from the list :")
#             add =input("enter the correct location :")
#             print(locations)
#             if demo in locations:
#                 x=locations.index(demo)
#                 locations.pop(x)
#                 locations.insert(x,add)
#                 print(locations)
#             else:
#                 print("location not found")
#         if choice ==3:
#             delete=input("enter the location to be deleted :")
#             if delete in locations:
#                 locations.remove(delete)
#             else:
#                 print("location not found")
#     return locations


# no=0
# locations=["kollam","thiruvantapuram"]
# while no!=2:
#     no=int(input("to close press 2 :"))
#     if no==2 :
#         pass
#     else:
#         name, age, id_type = user()
#         if name == "god":
#             locations=admin()
#             continue
#         if check_user(name, age, id_type)==True:
#              check_bus_availability(locations)
            

#     output:to close press 2 :0
# Welcome to the Bus Ticket Booking System
# Enter your name: god
# Enter your age: 19
# Enter your ID type : Aadhar
# admin portal , used to update
# loacations are ['kollam', 'thiruvantapuram']
# enter a choice/n 1) press 1 to add locations /n2) press 2 to edit locations /n3)press 3 to remove locations /n4) press 4 to exit admin/n1
# enter location :aaluva
# enter a choice/n 1) press 1 to add locations /n2) press 2 to edit locations /n3)press 3 to remove locations /n4) press 4 to exit admin/n4
# to close press 2 :0
# Welcome to the Bus Ticket Booking System
# Enter your name: man
# Enter your age: 19
# Enter your ID type : Aadhar
# stops are['kollam', 'thiruvantapuram', 'aaluva']
# enter pick_up point :aaluva
# enter destination :kollam
# enter the time for boarding10:30
# your bus is booked from aaluva to kollam at 10:30
# to close press 2 :2


