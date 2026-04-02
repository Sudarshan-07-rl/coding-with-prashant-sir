#WAP to accept phy, chem and math subject marks . Calculate the total and percentage of marks and if greater than equal to 60 and gender is equal to make so he is eligible for placement else eligible for data entry job.
phy = int(input("Enter the marks of physics: "))
chem = int(input("Enter the marks of chemistry: "))
math = int(input("Enter the marks of mathematics: "))
gender = input("Enter your gender(male/female) : ")

total = phy + chem + math
print("Total: ", total)
percentage = (total / 300) * 100
print("Percentage: ", percentage)

if percentage >= 60 and gender == "male":
    print("You are eligible for placement.")
else:
    print("You are eligible for a data entry job.")