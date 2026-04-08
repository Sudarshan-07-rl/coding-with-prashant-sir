# constant time complexity
# it takes constant time to execute any element access operation    
# arr = [1, 2, 3, 4, 5]
# print(arr[0])

#============================================================================================================
#linear time complexity
# it takes linear time to execute any iteration operation
# arr = [1, 2, 3, 4, 5]
# for element in arr:
#     print(element)

#============================================================================================================
#logarithmic time complexity   
# it takes logarithmic time to execute any binary search operation
# arr = [1, 2, 3, 4, 5]
# for i in range(0, len(arr), 2):
#     print(arr[i])

#============================================================================================================
#quadratic time complexity
# it takes quadratic time to execute any nested iteration operation
# for 2 loops O(n^2) it gives n*n results
# looking arr in every arr element

# arr = [1, 2, 3, 4, 5]
# for x in arr:
#     for y in arr:
#         print(x, y)


#for 3 loops O(n^3) it gives n*n*n results
# arr = [1, 2, 3, 4, 5]
# for x in arr:
#     for y in arr:
#         for z in arr:
#             print(x, y, z)

#for multiple loops O(n^m) it gives n*n*n...m times results

#============================================================================================================

# O(2^n): Exponential Time Complexity
# This is common in recursive algorithms that solve "all possible combinations" problems.
# The runtime grows exponentially with the input size, making it impractical for large inputs.
# Example: Calculating the nth Fibonacci number using naive recursion
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
# print(fibonacci(10))  # This will take a long time for larger values of n

#============================================================================================================
# STACK

# Stack is a linear data structure that follows the Last In First Out (LIFO) principle.
# Stack operations:
#   - Push: Add an element to the top of the stack
#   - Pop: Remove an element from the top of the stack
#   - Peek: Get the top element without removing it
#   - Is Empty: Check if the stack is empty
#   - Is Full: Check if the stack is full
#   - Delete: Delete the entire stack

# Stack is implemented by 2 ways 
# 1. Array
# 2. Linked List 

# Stack using List :
#       - Easy to implement
#       - Speed problem when it grows

# Stack using Linked List :
#       - Fast performance
#       - Memory unflexible
#       - Implementation is not easy

# Stack time and Space complexity
# O(1) - create a stack            - O(1)
# O(1)/O(N^2) - push an element    - O(1)
# O(1) - pop an element            - O(1)
# O(1) - peek an element           - O(1)
# O(1) - is empty                  - O(1)
# O(1) - is full                   - O(1)
# O(1) - Delete entire stack       - O(1)

#============================================================================================================

# Queue

# Queue is a linear data structure that follows the First In First Out (FIFO) principle.
# The operations performed on the queue are:
#   - Enqueue: Adding an element to the queue
#   - Dequeue: Removing an element from the queue
#   - Front: Getting the front element of the queue
#   - Rear: Getting the rear element of the queue
#   - Is Empty: Check if the queue is empty
#   - Is Full: Check if the queue is full
#   - Delete: Delete the entire queue

# Queue is implemented by 2 ways 
# 1. Array
# 2. Linked List

# Queue using list:
#       - Easy to implement
#       - Speed problem when it grows

# Queue using linked list:
#       - Fast performance
#       - Memory unflexible
#       - Implementation is not easy

# Queue time and Space complexity
# O(n) - create a queue       - O(1)
# O(n) - enqueue an element   - O(1)
# O(n) - dequeue an element   - O(1)
# O(1) - peek an element      - O(1)
# O(1) - is empty             - O(1)
# O(1) - is full              - O(1)
# O(1) - Delete entire queue  - O(1)

#==================================== Example of time complxity =============================================
# sample array example
# find biggest number in a list

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,111,5,7,78,54,32,45,67,89,95,23,45,67,89,90]
# def find_biggest_number(arr):
#     first_element = arr[0] # first element = 1 // time_complexity ==> O(1)
#     for i in range(1, len(arr)): # time_complexity ==> O(n)
#         if arr[i] > first_element: # time_complexity ==> O(1)
#             first_element = arr[i] # time_complexity ==> O(1)
#     return first_element # time_complexity ==> O(1)

# print("Biggest number in the list is:", find_biggest_number(a)) # time_complexity ==> O(1)
# final time complexity is O(1) + O(n) * O(1) + O(1) = O(n)
# Because O(1) is constant, it can be ignored
# So the final time complexity is O(n)

#============================================================================================================

