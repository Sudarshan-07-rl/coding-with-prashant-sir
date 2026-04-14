# Points

# Racursion

# Space efficient?

# No

# Yes

# No stack memory require in case of leration

# Time efficient?

# No

# Yes

# in case of recursion system needs more time for pop and push elements to stack memory which make recursion less time efficient

# Easy to code?

# Yes

# No

# We use recursion especially in the cases we kno that a problem can be divided ando sentar sub problems



####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Factorial solution 
# def factorial(num):
#     if num <= 1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(4))

#####-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def isPalindrome(string):
#     if len(string) == 0:
#         return True
#     if string(0) != string[len(string)-1]:
#         retrun False
#     return isPalindrome(string[1:-1])
          
# print(isPalindrome('awesome'))
# print(isPalindrome('footbar'))
# print(isPalindrome('tacocat'))

######----------------------------------------------------------------------------------------------------------------------------------------------------------

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent -1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

####---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def capitalizefirst(arr):
    
#     result = []
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizefirst(arr[1:])

# print(capitalizefirst(['car', 'taco', 'banana']))

###---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))

#####-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def fib(num):
#     if (num < 2):
#         return num
#     return fib(num - 1) + fib(num -2)

# print(fib(4))

######----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

