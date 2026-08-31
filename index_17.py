# class dog:
#     def bark(self):
#         print ("dog barks ")
# dog=dog()
# dog.bark()


# # instance attributes , class attributes
# class student:
#     # course="python" class attributes
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
# s=student("god",80)
# print(s.name,s.mark) 

# print(s.course)
# # s1=student("man",50)instance attributes
# print(s1.name,s1.mark,s1.course)  





# acess modifier 
class modifier:
    public=1
    _protected=2
    __private=3
    def show(self):
        print(self.__private)
m=modifier()
print(m.public)
print(m._protected)