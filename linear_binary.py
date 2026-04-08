#=================================================================
# LINEAR SEARCH
#=================================================================
#=============================Example=============================

# def linear_search(array, target):# o(n)
#     for i in range(len(array)):# o(n)
#         if array[i] == target:# o(1)
#             return i
#     return -1

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # o(n)
# target = 55 # o(1)
# result = linear_search(array, target) # o(n)
# if result == -1: # o(1)
#     print("Element not found") # o(1)
# else:
#     print("Element found at index No :", result) # o(1)

#=================================================================

#=================================================================
# BINARY SEARCH
#=================================================================
#=============================Example============================= 

# Binary Search implementation without recursion
# def binary_search(array, target):# o(log n)
#     start = 0
#     end = len(array) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # o(n)
# target = 5 # o(1)
# result = binary_search(array, target) # o(log n)
# if result == -1: # o(1)
#     print("Element not found") # o(1)
# else:
#     print("Element found at index No :", result) # o(1)

#====================================================================
