# sets
# nums={1, 2, 3, 4, 2}
# print(nums)
# output:{1, 2, 3, 4}


# nums=set([1, 2, 3, 4,])
# print(nums)
# print(type(nums))



# empty={}
# emppty1=set()
# print(type(empty)) class dict 
# print(type(emppty1)) class set


# nums={1, 2, 3, 4, 2}
# print(nums[0]) does not support indexing



# acessing elements in sets 
# nums={1, 2, 3, 4, 2}
# for item in nums:
#     print(item)



# add elements to set
# nums={1, 2, 3, 4,}
# nums.add(5)
# print(nums)



# udate , to add multiple elements to sets
# nums={1, 2, 3, 4,}
# nums.update({5, 6, 7})
# print(nums)





# to remove elements from sets
# nums={1, 2, 3, 4,}
# nums.remove(5)
# print(nums)
 



# nums={1, 2, 3, 4,}
# nums.discard(5)
# print(nums)




# nums={1, 2, 3, 4,}
# nums.pop()
# # print(x)
# print(nums)




# nums={1, 2, 3, 4,}
# print(nums)
# nums.clear()
# print(nums)






# set operations
# union
# a={1, 2, 3, 4,}
# b={3, 4, 5, 6,}
# print(a|b)
# print(a.union(b))

# intersection
# a={1, 2, 3, 4,}
# b={3, 4, 5, 6,}
# print(a&b)
# print(a.intersection(b))



 # difference
# a={1, 2, 3, 4,}
# b={3, 4, 5, 6,}
# print(a-b)
# print(a.difference(b))


# symmetric difference
# a={1, 2, 3, 4,}
# b={3, 4, 5, 6,}
# print(a^b)
# print(a.symmetric_difference(b))






# membership testing
# nums={1, 2, 3, 4,}
# print(2 in nums)
# print(5 in nums)



# iteration 
# nums={1, 2, 3, 4,}
# for item in nums:
#     print(item)




# nums=frozenset([1, 2, 3, 4,])
# nums.add(5) # frozenset is immutable, so it does not support add or remove operations
# print(nums)





# dictionary
# students={
#     "name":"john",
#     "age":20,
#     "course":"python"
# }
# print(students)



# repetition
# values
# data={
#     "a": 100,
#     "b": 100
# }
# print(data)


# # keys
# students={
#     "name":"john",
#     "name":"doe"
#  }output is corrupt , duplicate keys are not allowed, the last value will be used
# print(students) # output: {'name': 'doe'} , duplicate keys are not allowed, the last value will be used



# using dict()
# person=dict(
#     name="john",
#     city="new york",
#     age=30
# )
# print (person)



# empty dictionary
# data={}



# aceesing elements in dictionary
# students={
#     "name":"john",
#     "age":20,
#     "course":"python"
# }   
# print(students["course"]) # output: python

# data=dict(
#     name="john",
#     age=20,
#     course="python"
# )
# print(data.get("roll_no"))



# udating elements in dictionary
# data={
#     "name":"john",
#     "age":20,
#     "course":"python"   
# }
# print(data)
# data["age"]=21
# print(data)
# using update() method to update multiple elements in dictionary
# data.update({
#     "age":22,
#     "course":"java" 
# })
# print(data)





# pop() method to remove elements from dictionary
# students={
#     "name":"john",
#     "age":20,
#     "course":"python"
# }
# print(students)
# x=students.pop("age")
# print(x)
# print(students)


# popitem()
# students={
#     "name":"john",
#     "age":20,
#     "course":"python"
# }
# print(students)
# x=students.popitem()
# print(x)
# print(students)




# del 
# students={
#     "name":"john",
#     "age":20,
#     "course":"python"
# }
# print(students)
# print(del students["age"])
# print(students)





# students={
#     "name":"john",
#     "age":20,
#     "course":"python"
# }
# print(students.keys())
# print(students.values())
# print(students.items())


# students={
#     "name":"john",
#     "age":20,
#     "course":"python"
# }
# # for key in students:
#     print(key)
# for value in students:
#     print(value)
# for key,value in students.items():
#     print(key,value)
# print("name" in students) 
# output: True
# print ("john"in students.values())
# output: True





# mixed data types
# data={1:"one",
#       "two":2,
#       (3,4):"tuple"
#       }
# print(data)
# print(data[(3,4)])





# nested dictionary
# students={
#     "name":"john",
#     "marks":{
#         "maths":90,
#         "science":80
#     }
# }
# # print(students)
# print(students["marks"]["maths"])