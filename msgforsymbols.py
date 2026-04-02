#WAP accept input character and check whether it is in uppercase,Lowercase,logical or numeric and specialcharacters.
ch = ord(input("Enter a character: "))
#ord() function is used to convert in ASCII value.
if 65 <= ch <= 90:
    print("The character is in uppercase.")
elif 97 <= ch <= 122:
    print("The character is in lowercase.")
elif 48 <= ch <= 57:
    print("The character is numeric.")
else:
    print("The character is a special character.")