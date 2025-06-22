"""
# Given an array arr of N integers. Find the maximum product of a subarray in the array.
# Examples:
# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 42
# Explanation: The subarray {2, 3, -8, 7} has the largest product 42.
"""


# Approach: max min product tracking
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
			temp1= max_ * arr[i]
			temp2 = min_ * arr[i]
			max_ = max(temp1, temp2, arr[i])
			min_ = min(temp1, temp2, arr[i])
			res = max(max_, min_, res)
		    
		
		return res
	

# Appraoch 2: Travelling from both sides

class Solution:
	def maxProduct(self,arr):
		# code here
		res = float('-inf')
		l2r = 1
		r2l = 1
		n = len(arr)
		
		for i in range(len(arr)):
			
			if l2r == 0:
				l2r = 1
			if r2l == 0:
				r2l = 1
				
			l2r *= arr[i]
			r2l *= arr[n-i-1]
			res = max(res, l2r, r2l)
		
		return res