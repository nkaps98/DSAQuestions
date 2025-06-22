# Approach: Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# This approach sorts the input array and then iterates through it to find the first missing number
# that is greater than 0. It works well for small to moderate-sized arrays.
# However, it is not the most efficient solution for larger arrays due to the sorting step.
def missingnum(arr):

    arr.sort()

    res = 1

    for num in arr:
        if num == res:
            res += 1

        elif num > res:
            break

    return res


# Approach: Boolean Array
# Time Complexity: O(n)
# Space Complexity: O(n)
# This approach uses a boolean array to track the presence of numbers from 1 to n.
# It iterates through the input array, marking the presence of each number.
# After that, it checks the boolean array to find the first missing number.
# If all numbers from 1 to n are present, it returns n+1.
# This approach is straightforward and works well for small to moderate-sized arrays.
def missingnum(arr):
    n = len(arr)
    
    bool_arr = [False] * n
    
    for i in range(n):
        if 0 < arr[i] <= n:
            bool_arr[arr[i]-1] = True
            
    for i in range(1, n+1):
        if not bool_arr[i-1]:
            return i
            
    return n+1


# Approach: Cyclic Sort
# Time Complexity: O(n)
# Space Complexity: O(1)
# This approach uses cyclic sort to place each number in its correct position.
# It iterates through the array, swapping elements until each number is in its
# correct position. After sorting, it checks for the first missing number.
class Solution:
    def missingNumber(self,arr):
            #Your code here
            n = len(arr)
            
            for i in range(n):
                
                while 0 < arr[i] <= n and arr[arr[i]-1] != arr[i]:
                    temp = arr[i]
                    arr[i] = arr[arr[i]-1]
                    arr[arr[i]-1] = temp
                    
                    
            for i in range(1, n+1):
                if arr[i-1] != i:
                    return i
                    
                    
            return n+1