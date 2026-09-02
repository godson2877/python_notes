# instance method
# class Student:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(self.name)
# s=Student("sai")
# s.show()



# oops concept

class Bankacct:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount    
    def withdraw(self,amount):
        if amount>self.__balance:
            raise ValueError("insufficent balance")
        self.__balance-=amount
    def show_balance(self):
        print(self.__balance)

b=Bankacct(1000)
b.show_balance()
b.withdraw(500)
b.show_balance()
