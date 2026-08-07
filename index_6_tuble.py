# normal tuple
# numbers1=(1,2,3,4,5)
# print(type(numbers1))
# num2=[6,7,8,9,10]
# print(type(num2))



# empty tuple
# num=()
# print(type(num))



# single element tuple
# t1=(3,)
# print(type(t1))  

# tuple packing
# a=1,2,3
# print(type(a))


# tuple unpacking
# a=(10,20)
# x,y,z=a
# print(x,y,z)




# a=(1,2,3,4,5,6)
# print(a[::-1])
# print(a)
# print(a[:3])




# immutable
# colors=("red","green","blue")
# colors[0]="yellow"
# print(colors)





# iteration
# colors=("red","blue","green")
# for i in range (len(colors)):
#     print(colors[i])


# tuple unpacking
# student=("god",21)
# name,age=student
# print (f"name:{name},age:{age}")




# extended unpacking
# num={1,2,3,4,5,6,7,8}
# a,b,*c=num
# print(f"a:{a},b:{b},c:{c}")


# list - tuple conversion
l1=[1,2,3,4,5]
t1=tuple(l1)
print(t1)
l1=list(t1)
print(l1)