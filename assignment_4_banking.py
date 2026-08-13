# banking system
user_id=99
i=0
user_data = []
user_data.append(data[i])
def create_acount():
    global i
    i+=1
    print("Creating a new account...")
    usr_age=int(input("Enter your age: "))
    if usr_age<18:
        print("You are not eligible to create an account.")
        return None
    user_name=input("Enter your name: ")
    account_type=input("Enter account type (savings/current): ")
    global user_id  
    user_id+=1
    data={}
    data[i]={
        "name":"user_name",
        "age":"usr_age",
        "id":"user_id"
    }

    return data[i]



