# def login(username,password):
    # if username == password:
        # print('login successfully')
    # else:
        # print('invalid credintials')
        # 
# username = input("enter username:")
# password = input("enter password:")
# login(username,password)
#---------------------------------------------------------------------------------------------

#default argument
# def cityname(city="Goa"):
    # print(city)
    # 
# cityname("Dharashiv")
# cityname("padoli")
# cityname()

#----------------------------------------------------------------------------------------------

#varible length argument
# def nameofCities(*City):
    # print("City Name's=",City)
# nameofCities("Goa","padoli","Dharashiv")

#----------------------------------------------------------------------------------------------

#WAP for menu driven code
# import sys
# def add():
    # val1 = int(input("Enter val1 : "))
    # val2 = int(input("Enter val2 : "))
    # print("add = ",val1+val2)
# 
# def sub():
    # val1 = int(input("Enter val1 : "))
    # val2 = int(input("Enter val2 : "))
    # print("sub = ",val1-val2)
# 
# def mul():
    # val1 = int(input("Enter val1 : "))
    # val2 = int(input("Enter val2 : "))
    # print("mul = ",val1*val2)
# 
# def div():
    # val1 = int(input("Enter val1 : "))
    # val2 = int(input("Enter val2 : "))
    # print("div = ",val1/val2)
# 
# while True:
    # print("1.Addition")
    # print("2.Substraction")
    # print("3.multiplication")
    # print("4.Division")
    # print("5.Exit")
    # choice = int(input("Enter the choice : "))
    # if choice == 1:
        # add()
    # elif choice == 2:
        # sub()
    # elif choice == 3:
        # mul()
    # elif choice == 4:
        # div()
    # elif choice == 5:
        # sys.exit()

#----------------------------------------------------------------------------------------------
#strip
programming  = input("Enter your programming Nmae : ")
p_name = programming.rstrip()
if p_name == 'python':
    print(p_name)
elif p_name == 'java':
    print(p_name)
elif p_name == 'cpp':
    print(p_name)
else:
    print("Wrong programming Name")