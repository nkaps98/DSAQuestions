"""
Move All Zeroes to End
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.
"""

# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach:
# 1. Initialize a variable `zero_index` to None, which will keep track of the index of the first zero found.
# 2. Iterate through the array using a while loop.
# 3. If the current element is zero and `zero_index` is None, set `zero_index` to the current index.
# 4. If the current element is non-zero and `zero_index` is not None, swap the current element with the element at `zero_index`, then increment `zero_index`.   

class Solution:
	def pushZerosToEnd(self, arr):
		zero_index = None
		i = 0
		while i < len(arr):
			if arr[i] == 0:
				if zero_index == None:
					zero_index = i
			elif arr[i] != 0 and zero_index != None:
				temp = arr[i]
				arr[i] = arr[zero_index]
				arr[zero_index] = temp
				zero_index += 1
				continue
			i += 1

		return arr