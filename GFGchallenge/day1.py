"""
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Example 1:
Input:
arr = [2, 3, 1, 4, 5]
Output:
4
"""

# Approach 1: 2 iterations
# Time Complexity: O(2n) similar to O(n)
# Space Complexity: O(1)

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        # arr = set(arr)
        maxm = -1
        for i in range(len(arr)):
            if arr[i] > maxm:
                maxm = arr[i]
                
        if maxm == -1:
            return -1
            
        diff = float('inf')
        second_max = -1
        for i in range(len(arr)):
            if (maxm - arr[i]) == 0:
                continue
            if abs(maxm - arr[i]) < diff:
                diff = abs(maxm - arr[i])
                second_max = arr[i]
                
        return second_max
    

# Approach 2: 1 iteration, better than Approach 1
# Time Complexity: O(n)
# Space Complexity: O(1)

# 1. Find the maximum element in the array.
# 2. Find the second maximum element by checking if the current element is less than the maximum and greater than the second maximum.
# 3. If the second maximum is not found, return -1.
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        # arr = set(arr)
        maxm = float('-inf')
        second_max = float('-inf')
        for i in range(len(arr)):
            if arr[i] > maxm:
                prev_max = maxm
                maxm = arr[i]
                
            if arr[i] > second_max and arr[i] < maxm:
                second_max = arr[i]
                
            if prev_max > second_max:
                second_max = prev_max
                
        if second_max == float('-inf'):
            return -1
            
        return second_max