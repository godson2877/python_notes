# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# c=a//b
# print(c)



try:
    a=10
    b=0
    if b==0:
        raise ZeroDivisionError("b cannot be zero")
    result=a/b
except ZeroDivisionError as e:
    print("cannot divide by zero ",e)
except Exception as e:
    print(" unexpected error: ",e)
else:
    print("result is: ",result)
finally:
    print("cleanup complete")