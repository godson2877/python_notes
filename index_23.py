def age_checker(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
try:
    print(age_checker(-90))
except ValueError as e :
    print("not possible")
finally:
    print("cleanup complete")