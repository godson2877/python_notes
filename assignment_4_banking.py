# banking system

def create_acount():
    print("Creating a new account...")
    usr_age=int(input("Enter your age: "))
    if usr_age<18:
        print("You are not eligible to create an account.")
        return None
    user_name=input("Enter your name: ").title
    user_pin=int(input("enter pin"))
    account_type=input("Enter account type (savings/current): ").title
    deposit=int(input("enetr intial amount"))
    global user_id  
    user_id+=1
    print (f"user id : {user_id}")
    data[user_id] = {
        "user_name":user_name,
        "user_id":user_id,
        "acc_type":account_type,
        "user_pin":user_pin,
        "balance":deposit,
        "transaction_history":[f"amount deposited with intial balance{deposit}"]
    }
 
def deposit_amount(x):
    pin=int(input("enter user pin"))
    if pin != data[x]["user_pin"]:
        print("entery restricted")
        return None
    balance=data[x]["balance"]
    amount=int(input("enter amount to be deposited "))
    balance+=amount
    data[x]["balance"]=balance
    print(f"balaance :{balance} ")
    data[x]["transaction_history"].append(f"deposited amount: {amount}")


def withdraw_amount(x):
    pin=int(input("enter user pin"))
    if pin != data[x]["user_pin"]:
        print("entery restricted")
        return None
    
    amount=int(input("enter amount to be withdrawed"))
    gst=gst(amount)
    amount_gst=amount+gst
    if  data[x]["balance"]<amount_gst:
        print("balance insufficent")
        return None
    print(f"amount: {amount},\ngst :{gst},\n total amount withdrawn:{amount_gst}")
    data[x]["balance"]-=amount
    data[x]["transaction_history"].append(f" amount: {amount},\ngst :{gst},\n total amount withdrawn:{amount_gst}")



def check_balance():
    x=int(input("enter user id :"))
    if x!=data[x]["user_id"]:
        return None
    pin=int(input("enter pin"))
    if pin!=data[x]["user_pin"]:
        return None
    print(f"balance: {data[x]["balance"]}")

def transaction_history():
    x=int(input("enter user id :"))
    if data[x]["user_id"]!=x:
        return None
    pin=int(input("enter pin"))
    if data[x]["user_pin"]!=pin:
        return None
    user_history=data[x]["transaction_history"]
    print (user_history)

def check_loan_eligibility():
    x=int(input("enter user id"))
    if x not in data:
        return None
    pin =int(input("enter pin"))
    if pin != data[x]["user_pin"]:
        return None
    loan_multiplier=3
    if data[x]["balance"]<1000:
        print(f"user {data[x]["user_name"]} does not have sufficent balance")
        return None
    print(f"user: {data[x]["user_name"]} can apply for loan upto {data[x]["balance"]*loan_multiplier}")





data={}
user_id=99
choice=0
gst=lambda amount:amount*0.18
while True:
    print("enter  a choice :\n1)create account\n2)deposit amount\n3)check balance \n4) transaction history  \n5)withdraw amount \n6)check loan availability \n7)exit ")
    choice=int(input("enter a choice :"))
    if choice == 1:
        create_acount()
        if create_acount==None:
            continue
    if choice==2:
        x=int(input("enter user id : "))
        deposit_amount(x)
        if deposit_amount==None:
            continue
    if choice ==3:
        check_balance()
        if(check_balance==None):
            continue
    if choice==4:
        transaction_history()
        if transaction_history==None:
            continue
    if choice==5:
        x=int(input("enter user id "))
        withdraw_amount(x)
        if withdraw_amount==None:
            continue
    if choice==6:
        break