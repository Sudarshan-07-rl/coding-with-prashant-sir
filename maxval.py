#Wap to accept value of A, B and C. Find the maximum value.
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
C = int(input("Enter the value of C: "))
if A>B:
    if A>C:
        print("A is the maximum value.")
    else:
        print("C is the maximum value.")
else:
    if B>C:
        print("B is the maximum value.")
    else:
        print("C is the maximum value.")