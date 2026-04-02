#WAP to change calculation with respect to total amount.
amount = int(input("Enter the total amount: "))
print("500 notes =", amount//500)
print("200 notes =", (amount%500)//200)
print("100 notes =", ((amount%500)%200)//100)
print("50 notes =", (((amount%500)%200)%100)//50)
print("20 notes =", ((((amount%500)%200)%100)%50)//20)
print("10 notes =", (((((amount%500)%200)%100)%50)%20)//10)
print("5 notes =", ((((((amount%500)%200)%100)%50)%20)%10)//5)