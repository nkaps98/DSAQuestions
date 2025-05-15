from typing import List
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# The solution should be done in O(n) time complexity and O(1) space complexity.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given a sorted list of integers, returns a list of the squares of each number,
        also sorted in non-decreasing order.

        Approach:
        - Square all elements in-place.
        - Use a two-pointer technique to sort the squared values in a new array.
        - Initialize two pointers: 'start' at the beginning and 'end' at the end of the array.
        - Compare the squared values from both ends, placing the larger one at the end of the result array.
        - Move the corresponding pointer and fill the result array from end to start.

        This works because the largest squared values will come from either the leftmost
        (most negative) or rightmost (most positive) numbers in the original array.

        Time Complexity: O(n)
        Space Complexity: O(n) for the result array

        Args:
            nums (List[int]): A list of integers sorted in non-decreasing order.

        Returns:
            List[int]: A list of squared integers sorted in non-decreasing order.
        """
        new_array = [0]*len(nums)

        for i in range(len(nums)):
            nums[i]*=nums[i]

        i = len(nums)-1

        start = 0
        end = len(nums)-1

        while start <= end:
            if nums[start] < nums[end]:
                new_array[i] = nums[end]
                end -= 1
            else:
                new_array[i] = nums[start]
                start += 1
            i-=1
        return new_array