# class student:
#     name="rex"
# s=student()
# print(s.name)



# class example:
#     __private =3
# e=example()

# # print(e.__private)
# print(e._example__private)

# class account:
#     _balance=1000
# class savingsaccount(account):
#     def show_balance(self):
#         print(self._balance)
# acc = savingsaccount()
# acc.show_balance()
# print(acc._balance)

# 1)single inheritance


# class animal:
#     def speak(self):
#         print("animal speaks")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
# d=dog()
# d.speak()
# d.bark()

# 2)multilevel inheritance

# class animal:
#     def speak(self):
#         print("animals make a sound")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
# class puppy(dog):
#     def cry(self):
#         print("puppy cries")
# p=puppy()
# p.cry()
# p.bark()
# p.speak()


# 3) heiarchial inheritance 
# class animal:
#     def speak(self):
#         print("animal speaks")
# class dog(animal):
#     def bark(self):
#         print("dog barks")
# class cat(animal):
#     def meow(self):
#         print("cat meows")
# cat=cat()
# cat.meow()
# cat.speak()
# dog=dog()
# dog.bark()
# dog.speak()



# 4) multiple inheritance

# class father:
#     def drive(self):
#         print("fathr can drive")
# class mother :
#     def cooking(self):
#         print("mother can cook")
# class child(father,mother):
#     pass
# child=child()
# child.cooking()
# child.drive()

# method resolution method



# super function 
# class animal:
#     def speak(self):
#         print("animal sound")
# class dog(animal):
#     def speak(self):
#         super().speak()
#         print("woof")
# d=dog()
# d.speak()




# class bankaccount:
#     account_holder="rex"
#     _balance=1000
#     __pin=2001
# bank=bankaccount()
# print(bank.account_holder)
# print(bank._balance)
# print(bank._bankaccount__pin)



# class person:
#     name="rex"
#     age=22
# class teacher(person):
#     subject="commerce"
# teach=teacher()
# print(teach.name)
# print(teach.age)
# print(teach.subject)