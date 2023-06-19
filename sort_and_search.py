def linear_search(arr, item): 
 
    for i in range(len(arr)):
        if arr[i] == item:
            return i    
    return None

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_search(arr, item): 

    low, high = 0, len(arr) - 1
    while high >= low:
        mid = (low + high) // 2
        if arr[mid] == item:
            print(arr[mid])
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

# 1:

# Linear search, as array list is not in order.
# Iterates through list and breaks when item is found.
# It has a time complexity of O(n), where n is the number
# of elements in the array.

# 2: Use linear search to search/find index for the number 9 in given
# array

arr  = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

linear_result = (linear_search(arr, 9))
print('\nLinear search result is:', linear_result)
# good to use linear search as the data is 
# unsorted and has a short/small array

# 3. Python program for implementation of Insertion Sort
# Ref: https://www.geeksforgeeks.org/insertion-sort/

insertion_sort(arr)
print("\nSorted Array is:", arr)

# 4. Use searching algorithm not tried in this task, Binary search

binary_result = binary_search(arr, 9)
print("\nBinary Search Result is:", binary_result)  

# Semiconductor test programs used for measuring digital timing or analog levels
# make extensive use of binary search or an a - z sorted list of say movies.