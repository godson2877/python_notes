# class File:
#     def read(self):
#         print("reading file")
# class Socket:
#     def read(self):
#         print("Reading socket")
# def fetch_data(source):
#     source.read()
# fetch_data( Socket())
# fetch_data(File() )    


# class Point:
#     def __init__(self, x):
#         self.x = x
#     def __add__(self,other):
#         return self.x + other.x
# p1= Point(10)
# p2= Point(20)
# print(p1+p2)



# class student:
#     def __init__(self):
#         self.__marks=0
#     @property
#     def marks(self):
#         return self.__marks
#     @marks.setter
#     def  marks(self, value):
#         if value < 0:
#             print("invalid marks")
#         else:
#             self.__marks =value
# s=student()
# s.marks  =-80
# print(s.marks)





# class student:
#     def __init__(self):
#          self.__marks=80
#     # def show_marks(self):
#     #      print(self.__marks)
#     def get_marks(self):
#          return self.__marks
#     def set_marks(self,value):
#          self.__marks=value
# s= student()
# print(s.get_marks())
# s.set_marks(100)
# print(s.get_marks())
# # print(s.__marks)
# # s.marks = 90
# # print(s.marks)