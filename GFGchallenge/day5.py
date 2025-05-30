# Next Permutation
"""
# Next Permutation
Given an array arr[] of size N, find the next permutation of the array in lexicographically increasing order.
If no such permutation exists, return the array sorted in ascending order.
# If the array is already sorted in descending order, return the array sorted in ascending order.
#
# Example 1:
Input: arr = [1, 2, 3]
Output: [1, 3, 2]
"""


# Approach:
# 1. Traverse the array from right to left to find the first pair of elements where the left element is smaller than the right element and make that the pivot.
# 2. If such a pivot is found, traverse the array from right to left again to find the smallest element that is larger than the pivot.
# 3. Swap the element at pivot with the above found element.
# 4. Reverse the subarray to the right of the pivot to get the next permutation.
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        
        pivot = -1
        
        # find the pivot
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
            
        # if pivot is -1, it means the array is sorted in ascending order 
        if pivot == -1:
            return arr.reverse()
            
        # find the smallest element larger than pivot from the right side
        for i in range(n-1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break
            
        right = n-1
        left = pivot + 1
        
        # reverse the subarray to the right of pivot
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            
            right -= 1
            left += 1
            
        return arr
        
                
                