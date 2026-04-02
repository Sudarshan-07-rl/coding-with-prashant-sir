#WAP to accept five numbers and find the maximum number among them.
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))
n5 = int(input("Enter the fifth number: "))

if (n1 >= n2) and (n1 >= n3) and (n1 >= n4) and (n1 >= n5):
    print("The maximum number is: ", n1)
if (n2 >= n1) and (n2 >= n3) and (n2 >= n4) and (n2 >= n5):
    print("The maximum number is: ", n2)
if (n3 >= n1) and (n3 >= n2) and (n3 >= n4) and (n3 >= n5):
    print("The maximum number is: ", n3)
if (n4 >= n1) and (n4 >= n2) and (n4 >= n3) and (n4 >= n5):
    print("The maximum number is: ", n4)
if (n5 >= n1) and (n5 >= n2) and (n5 >= n3) and (n5 >= n4):
    print("The maximum number is: ", n5)