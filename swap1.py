val1 = int(input("Enter the value of val1: "))
val2 = int(input("Enter the value of val2: "))
print("Before swapping val1=", val1,"and val2=", val2)
val1 = val1 + val2
val2 = val1 - val2
val1 = val1 - val2
print("After swapping val1=", val1,"and val2=", val2)