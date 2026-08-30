# 1)
# text=input("enter a word")
# count={}
# for ch in count:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print (count)


# 2)
# text=input("enter a word")
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# lowest=count[ch]
# frequency=""
# for ch in count:
#     if count[ch]<lowest:
#         lowest=count[ch]
#         frequency=ch
# print(f"least frequent character:{frequency}, no of times: {lowest}")


# 3)
# text=input("enter a word :")
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# for ch in count:
#     if count[ch]>1:
#         print(f"characther: {ch},count:{count[ch]}")



# 4)
# text=input("enter a word :")
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# for ch in count:
#     if count[ch]==1:
#         print(f"characther :{ch}, count:{count[ch]}")



# 5)
# text = input("enter the string   ")
# count={}
# for ch in text:
#     if ch in count:
#         firstchar = ch
#         break
#     else:
#         count[ch]=1
# print(" 1st repeated frequency is",firstchar)


# 6)
# text =input("enter a word")
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#          count[ch]=1
# for ch in count:
#     if count[ch]==1:
#         print(f"characther :{ch},count:{count[ch]}")
#         break



# 7)
# text =input("enter a word")
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#          count[ch]=1
# highest=0
# ch_1="" 
# medium=0
# ch_2=""  
# for key,value in count.items():
#     if value>highest:
#         medium=highest
#         ch_2=ch_1
#         highest=value
#         ch_1=key
#     elif value>medium:
#         medium=value
#         ch_2=key
# print(f"the second most frequen characthers are {ch_2}  with count {medium}")



# 8)
# text = input("enter the string")
# uniquelist = []
# uniquecount = 0

# for ch in text:
#     if ch not in uniquelist:
#         uniquelist.append(ch)
#         uniquecount += 1

# print("Unique characters:", uniquelist)
# print("Number of unique characters:", uniquecount)

# 9)
# numbers = [10, 20, 10, 30, 20, 10, 40]
# freq = {}
# for num in numbers:
#     if num in freq:
#         freq[num] = freq[num] + 1
#     else:
#         freq[num] = 1
# most_frequent = None
# highest = 0
# for num in freq:
#     if freq[num] > highest:
#         highest = freq[num]
#         most_frequent = num
# print("Most Frequent Number:", most_frequent)



# 10)
# numbers=[]
# n=int(input("enter the no of numbers to  input:"))
# for i in range (n):
#     no=int(input(f"enter no at pos:{i+1}"))
#     numbers.append(no)
# count={}
# for num in numbers:
#     if num in count:
#         count[num]+=1
#     else:
#         count[num]=1
# lowest=count[num]
# freq=num
# for key,value in count.items():
#     if lowest>value:
#         lowest=value
#         freq=key
# print(f"the lowest frequent no are :{freq} and the count is {lowest}")




# 11)#most purchased items
# Orders = ["Laptop", "Mouse", "Laptop", "Keyboard", "Mouse", "Laptop"]
# counts = {}
# maxitem = 0
# maxcount = 0
# for item in Orders:
#     if item in counts:
#         counts[item] += 1
#     else:
#         counts[item] = 1
#     if counts[item] > maxcount:
#         maxcount = counts[item]
#         maxitem = item

# print("   ", maxitem)


# 12)
# votes = ["A", "B", "A", "C", "B", "A", "B"]
# counts = {}
# max_item = None
# max_count = 0
# for vote in votes:
#     if vote in counts:
#         counts[vote] += 1
#     else:
#         counts[vote] = 1
#     if counts[vote] > max_count:
#         max_count = counts[vote]
#         max_item = vote

# print(max_item)



# 13)
# text="apple mango apple orange mango apple"
# words=text.split()
# count={}
# for word in words :
#     if word in count:
#         count[word]+=1
#     else:
#         count[word]=1
# highest=0
# freq=""
# for key,value in count.items():
#     if value>highest:
#         highest=value
#         freq=key
# print(f"the most frequent word is {freq} and the count is {highest}")




# 14)
# names = ["Anu", "Rahul", "Anu", "Meera", "Rahul", "Anu"]
# counts = {}
# max_item = None
# max_count = 0
# for name in names:
#     if name in counts:
#         counts[name] += 1
#     else:
#         counts[name] = 1
#     if counts[name] > max_count:
#         max_count = counts[name]
#         max_item = name

# print(max_item)


# 15)
# errors = [404, 500, 404, 403, 404, 500]
# counts = {}
# max_item = None
# max_count = 0
# for error in errors:
#     if error in counts:
#         counts[error] += 1
#     else:
#         counts[error] = 1
#     if counts[error] > max_count:
#         max_count = counts[error]
#         max_item = error

# print(max_item)


