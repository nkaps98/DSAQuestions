"""
# Given an array arr of N integers. Find the maximum product of a subarray in the array.
# Examples:
# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 42
# Explanation: The subarray {2, 3, -8, 7} has the largest product 42.
"""


# Approach: One pass solution
# 1. Initialize two variables, max_ and min_, to the first element of the array.
# 2. Initialize a variable res to the first element of the array.
# 3. Iterate through the array starting from the second element.
# 4. For each element, calculate the maximum and minimum products by considering both the current element and the product of the current element with max_ and min_.
# 5. Update max_ to be the maximum of the calculated products.
# 6. Update min_ to be the minimum of the calculated products.
# 7. Update res to be the maximum of res, max_, and min_.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
	def maxProduct(self,arr):
		# code here
		max_ = arr[0]
		min_ = arr[0]
		res = arr[0]
		
		for i in range(1, len(arr)):
			temp1_1, temp1_2 = max_ * arr[i], arr[i]
			temp2_1, temp2_2 = min_ * arr[i], arr[i]
			max_ = max(temp1_1, temp1_2, temp2_1, temp2_2)
			min_ = min(temp1_1, temp1_2, temp2_1, temp2_2)
			res = max(max_, min_, res)
		    
		
		return res