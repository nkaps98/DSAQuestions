"""
Leet code 1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
You can follow up with how many ways you can solve this problem.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Problem link:https://leetcode.com/problems/two-sum/submissions/1626679511
"""

from typing import List


# Approach 1: Brute force
# Time complexity: O(n^2)
# Space complexity: O(1)
# We can use a nested loop to iterate through the list and check if any two numbers add up to the target.
# This approach has a time complexity of O(n^2) and a space complexity of O(1).
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            while start <= end:
                temp_start_sum = nums[i] + nums[start]
                temp_end_sum = nums[i] + nums[end]
                if temp_end_sum == target:
                    return [i, end]
                elif temp_start_sum == target:
                    return [i, start]
                start += 1
                end -= 1

# Approach 2: Dictionary
# We can use a dictionary to store the numbers and their indices as we iterate through the list.
# For each number, we check if the complement (target - number) exists in the dictionary.
# If it does, we return the indices of the current number and its complement.
# This approach has a time complexity of O(n) and a space complexity of O(n).
# Time complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_freq = {}

        for i in range(len(nums)):
            diff_val = target - nums[i]
            if diff_val in num_freq:
                return [i, num_freq[diff_val]]
            num_freq[nums[i]] = i
