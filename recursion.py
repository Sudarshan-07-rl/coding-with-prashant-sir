#=========================================================================================================
#=========================================================================================================

# Recursion: A function that calls itself
# it is not a efficient way to solve problems
# but it is a easy way to solve problems
# it is used in divide and conquer algorithms
# it is used in tree traversal
# it is used in graph traversal
# it is used in backtracking algorithms
# it is used in dynamic programming
# it is used in recursion

# Recursion uses call stack internally
# Call stack is a data structure that stores information about the active subroutines of a computer program
# Call stack is a stack data structure that stores information about the active subroutines of a computer program
# Call stack is a last in first out (LIFO) data structure
# Call stack is used to store information about the active subroutines of a computer program
# Call stack is used to manage function calls and returns

# Recursion Rules:
# 1. Identify the base case
# 2. Identify the recursive case
# 3. Return the correct value


# Time complexity: O(n)
# Space complexity: O(n)

#comparison between loop and recursion in table format
# | Loop                  | Recursion                |
# |-----------------------|--------------------------|
# | Time Complexity: O(n) | Time Complexity: O(n)    |
# | Space Complexity: O(1)| Space Complexity: O(n)   |

# Recursion and Iteration comparison
# |  Recursion    |  Iteration      |
# |---------------|-----------------|
# |  More memory  |  Less memory    |
# |  More time    |  Less time      |
# |  More space   |  Less space     |
# |  More readable|  Less readable  |

#============================================Factorial===========================================
# num = int(input("Enter a number: "))
# def factorial(n):
#     if n == 0:  # Base Condition
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(num))
# print(factorial(4))
# 2 * factorial(3)

#=========================================================================================================
#=========================================================================================================

#============================================Fibonacci Sequence===========================================
# num = int(input("Enter a number: "))
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(num))

#==========================================================================================================

#============================================Power of Two===========================================

# num = int(input("Enter a number: "))
# def poweroftwo(n):
#     if n == 0:
#         return 1
#     else:
#         power = poweroftwo(n-1)
#         return power * 2

# print(poweroftwo(num))

#==========================================================================================================
# Power of Two Iterative
# num = int(input("Enter a number: "))
# def powerofTwoIterative(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power * 2
#         i = i + 1
#     return power

# print(powerofTwoIterative(num))

#========================================================================================================
#========================================================================================================

#Is palindrome

# def isPalindrome(string):
#     if len(string) == 0:
#         return "String is palindrome"
    
#     if string[0] != string[-1]:
#         return "String is not palindrome"
#     return isPalindrome(string[1:-1])
       

# print(isPalindrome("racecar"))
# print(isPalindrome("hello"))
# print(isPalindrome("madam"))
# print(isPalindrome("noon"))
# print(isPalindrome("   "))

#==========================================================================================================
#==========================================================================================================

# def Power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base * Power(base, exponent-1) # 2 * Power(2, 2) -> 2 * 2 * Power(2, 1) -> 2 * 2 * 2 * Power(2, 0) -> 2 * 2 * 2 * 1 -> 8

# print(Power(2, 0))
# print(Power(2, 3))
# print(Power(3, 2))
# print(Power(5, 2))
# print(Power(2, 11))

#==========================================================================================================
#==========================================================================================================

#capitalize first letter of each word
# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0].capitalize())
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['hello', 'world', 'python', 'is', 'awesome', 'and', 'fun']))

#==========================================================================================================
#==========================================================================================================

# Product of Array
# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1, 2, 3, 4, 5]))
# print(productOfArray([1,2,3,10]))

#==========================================================================================================
#==========================================================================================================

# fib solution
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(4))
# print(fib(10))
# print(fib(28))
# print(fib(35))

#==========================================================================================================
#==========================================================================================================

