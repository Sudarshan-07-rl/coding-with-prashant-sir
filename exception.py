# n1 = int(input("Enter first value = "))
# n2 = int(input("Enter second value = "))
# try:
    # print(n1/n2)
# except:
    # print("can't dive by zero")
# print("to be continue......")

#---------------------------------------------------------------------------------
# try:
    # n1 = int(input("Enter first value = "))
    # n2 = int(input("Enter second value = "))
    # print(n1/n2)
# except ZeroDivisionError:
    # print("can't dive by zero")
# except ValueError:
    # print("Enter only integer value")
# print("To be continue...")

#--------------------------------------------------------------------------------

# try:
    # a = int(input("Enter first integer no = "))
    # b = int(input("Enter second integer no = "))
    # print(a/b)
# except(ValueError, ZeroDivisionError ) as message:
    # print(message)
    
#--------------------------------------------------------------------------------
#default except block
# try:
#     a = int(input("Enter first integer no = "))
#     b = int(input("Enter second integer no = "))
#     print(a/b)
# except(ValueError, ZeroDivisionError ) as message:
#     print("Enter correct number :",message)
# except:
#     print("This is defult part of except block")
#-------------------------------------------------------------------------------
# try:
#     a = int(input("Enter first integer no = "))
#     b = int(input("Enter second integer no = "))
#     print(a/b)
# except(ValueError, ZeroDivisionError ) as message:
#     print("Enter correct number :",message)
# else:
#     print("Everything is ok")
#-------------------------------------------------------------------------------
#finally block
# try:
#     a = int(input("Enter first integer no = "))
#     b = int(input("Enter second integer no = "))
#     print(a/b)
# except(ValueError, ZeroDivisionError ) as message:
#     print("Enter correct number :",message)
# finally:
#     print(" I will always executed")

#---------------------------------------------------------------------------------

#nested try except block
# try:
#     a = int(input("Enter first integer no = "))
#     b = int(input("Enter second integer no = "))
#     try:
#         print(a/b)
    
#     except ZeroDivisionError as message:
#         print(message)
# except ValueError as message:
#     print(message)
#-------------------------------------------------------------------------------------
# try:
#     a = int(input("Enter first integer no = "))
#     b = int(input("Enter second integer no = "))
#     print(a/b)
# except(ValueError, ZeroDivisionError ) as message:
#     print(message)
# else:
#     print("there are no error in try")
# finally:
#     print("I am always executed")
#-----------------------------------------------------------------------------------
# def security_key(n):
#     freq = {}
#     for i in str(n):
#         freq[i] = freq.get(i, 0) + 1
#     max_freq = max(freq.values())
#     return int(min(i for i in freq if freq[i] == max_freq))

# print(security_key(578378923))

#-----------------------------------------------------------------------------------
# a = [5,7,8,3,7,8,9,2,3]
# b = {}
# print(a)
# count = 0
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# print(b)
# for key, value in b.items():
#     if value > 1:
#         count += 1
# if count > 0:
#     print("Security key is: ", count)
# else:
#     print("Security key is: -1")

#---------------------------------------------------------------------------------------------
# a = [5,7,8,3,7,8,9,2,3]
# b = []

# for i in range(len(a)):
#     count = 0
#     key = a[i]
    
#     j = i+1
#     while j<len(a):
#         if key == a[j]:
#             b.append(key)
#         j = j+1
# print(len(b))
#-------------------------------------------------------------------------------------------
#access 2nd largest element
# a = [7,8,3,2,9,5]
# a.sort()
# print(a)
# print(a[-2])
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#while loop
#------------------------------------------------------------------------------------------
# 1
# i=1
# while i<=5:
#     print(i)
#     i += 1
#-------------------------------------------------------------------------------------------

#2
# username = ""
# password = ""
# while username !="admin" or password !="admin":
#     username = input("Enter username :")
#     password = input("Enter password :")
#-----------------------------------------------------------------------------------------
#vowel and consonant
# name = "programming"
# vowels = ['a','e','i','o','u']
# cons = 0
# vowel = 0
# for i in name:
#     if i in vowels:
#         vowel += 1
#     else:
#         cons += 1
# print("vowels =",vowel)
# print("cons =",cons)
#------------------------------------------------------------------------------------------

# Remove all occurance of an Element in list
# list = [1,2,2,3,4,2]
# print(list)
# newlist = []
# element = int(input("Enter the element to remove: "))
# for i in list:
#     if i != element:
#         newlist.append(i)
# print(newlist)
#-----------------------------------------------------------------------------------------

# list = [1,2,2,3,4,2]
# a = []
# element = int(input("Enter the element you want to remove ="))
# for i in list:
#     if i != element:
#         a.append(i)
# print(a)

