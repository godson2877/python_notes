# text=input("enter a word :")
# frequency={}

# for char in text:
#     if char in frequency:
#         frequency[char]+=1
#     else:
#         frequency[char]=1

# maxi = 0
# second=0
# freq = ""
# second_freq=""
# for key,value in frequency.items():
#     if maxi<value:
#         second=maxi
#         second_freq=freq
#         maxi=value
#         freq=key

#     elif value>second:
#         second=value
#         second_freq=key
        

# print("Most Frequent Character: ",freq," is repeated ",maxi," times.")

# print("Second Most Frequent Character: ",second_freq," is repeated ",second," times.")




# printing strs
# print("horizontal printing")
# for i in range(5):
#     print("*",end="")
# print("vertical printing")    
# for i in range (5):
#     print("*")

# for i in range (1,6):
#     for j in range(i):
#         print("*",end="")
#     print()


# for i in range (1,6,1):
#     print(i*"*")


# for i in range(1,7):
#     print()
#     for j in range(1,i+1):
#         print(j,end="")


# num=1
# for i in range(1,5):
#     print()
#     for j in range(1,i+1):
#         print(num,end="")
#         num+=1