# conditions
# 1)check whether the bus is available or not,check destination and source,check time of the bus
# 2)check whether the seat is available or not, user can only book the available seat and purcase upto 3 tickets 
# 3)check whether the user is student or not 
# 4)confirm payment
# 5)generate ticket


def user():
    print("Welcome to the Bus Ticket Booking System")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    id_type = input("Enter your ID type : ")
    return name, age, id_type

def check_user(name, age, id_type):
    if age<18:
        print(f" {name}, you are not eligible to book a ticket.")
        return False
    elif id_type not in ["Aadhar", "Voter ID", "Driving License"]:
        print(f"{name}, Invalid ID type. Please provide a valid ID.")
        return False
    return True

def check_bus_availability(locations):
    print(f"stops are{locations}")
    source=input("enter pick_up point :")
    destination=input("enter destination :")
    if source== destination:
        print ("invalid ")
    elif source not in locations and destination not in locations:
        print("invlaid")
    else:
        enter_time=input("enter the time for boarding")
        return enter_time


def admin():
    print("admin portal , used to update ")
    locations=["kollam","thiruvantapuram"]
    print (f"loacations are {locations}")
    choice =0
    while choice!=4:
        choice=int(input("enter a choice/n " 
        "1) press 1 to add locations /n" 
        "2) press 2 to edit locations /n"
        "3)press 3 to remove locations /n"
        "4) press 4 to exit admin/n"))
        if choice == 1:
            add = input("enter location :")
            locations.append(add)
        if choice == 2:
            demo=input("enter the location to be changed from the list :")
            add =input("enter the correct location :")
            print(locations)
            if demo in locations:
                x=locations.index(demo)
                locations.pop(x)
                locations.insert(x,add)
                print(locations)
            else:
                print("location not found")
        if choice ==3:
            delete=input("enter the location to be deleted :")
            if delete in locations:
                locations.remove(delete)
            else:
                print("location not found")
    return locations


no=0
locations=["kollam","thiruvantapuram"]
while no!=2:
    no=int(input("to close press 2 :"))
    if no==2 :
        pass
    else:
        name, age, id_type = user()
        if name == "god":
            locations=admin()
            continue
        check_user(name, age, id_type)
        enter_time= check_bus_availability(locations)
       


