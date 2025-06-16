"""
Given an integer array arr[]. You need to find the maximum sum of a subarray.

Examples:

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.
"""

# Approach: Kadane's Algorithm
# 1. Initialize two variables, max_sum and res, to the first element of the array.
# 2. Iterate through the array starting from the second element.
# 3. For each element, update max_sum to be the maximum of (max_sum + current element) and (current element).
# 4. Update res to be the maximum of res and max_sum.
# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List

class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        n = len(arr)
        max_sum = arr[0]
        res = arr[0]
        
        for i in range(1, len(arr)):
            max_sum = max(max_sum + arr[i], arr[i])
            
            res = max(res, max_sum)
            # print(max_sum, res)
        
        return res
            
        
                