#WAP to tell the day is weekend or working day.
day = input("Enter the day of the week: ")
valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
if day.lower() not in valid_days:
    print("Error: Please enter a valid day of the week.")
else:
    if day.lower() in ['saturday', 'sunday']:
        print(day, "is a weekend.")
    else:
        print(day, "is a working day.")