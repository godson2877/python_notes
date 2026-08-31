# polymorphism


# class dog :
#     def speak(self):
#         print("woof")
# class cat:
#     def speak(self):
#         print("meow")
# animals=[dog(),cat()]
# for a in animals:
#     a.speak()




# class car:
#     def move(self):
#         print("car is moving")
# class boat:
#     def move(self):
#         print("boat is moving")
# class bike :
#     def move(self):
#         print("bike is moving")
# vehicles=[car(),boat(),bike()]
# for a in vehicles:
#     a.move()


# ducktyping

# class file:
#     def read (self):
#         print("reading file")
# class socket:
#     def read(self):
#         print("reading socket")
# def fetch_data(source):
#     source.read()
# fetch_data(file())
# fetch_data(socket())



# operator overloading 


# class point:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x + other.x
# p1=point(10)
# p2=point(20)    
# print(p1+p2)

 

# encapsulation

# class student:
#     def __init__(self):
#         self.__marks=0
#     @property
#     def marks(self):
#         return self.__marks

#     @marks.setter
#     def marks(self,value):
#         if value<0:
#             print("invalid marks")
#         else:
#             self.__marks=value
# s=student()
# s.marks=-20
# print(s.marks)


# class student:
#     def __init__(self):
#         self.__marks=50
#     def showmarks(self):
#         print(self.__marks)
# s=student()
# s.showmarks()
# # print(s.__marks)
# # s.marks=90
# # print(s.marks)

# class student:
#     def __init__(self):
#         self.marks=50
#     def get_marks(self):
#         return self.marks
#     def set_marks(self,value):
#         self.marks=value
# s=student()
# print(s.get_marks())
# s.set_marks(100)
# print(s.get_marks())