"""
Reverse an Array
You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place
"""

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:

    def reverseArray(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        
        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            
            left += 1
            right -= 1
            
        return arr