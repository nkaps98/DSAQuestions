from typing import List
# Given an integer array nums of length n and an integer target, return the sum of the three integers such that they
# sum is closest to target and return the sum of the three integers.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# The solution should be done in O(n^2) time complexity and O(1) space complexity.
# Approach:
# 1. Sort the array to make it easier to avoid duplicates.
# 2. Use a for loop to iterate through the array.
# 3. For each element, use two pointers (left and right) to find pairs that sum to the negative of the current element.
# 4. If the sum of the triplet is closest to the target, update the closest sum.
# 5. Move the left pointer to the right and the right pointer to the left to find new pairs.

# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        min_diff = float('inf')

        for i in range(0, len(nums)-2):
            l = len(nums)-1
            r = i + 1
            while r < l:
                sums = nums[i] + nums[l] + nums[r]
                if abs(sums - target) < min_diff:
                    closest_sum = sums
                    min_diff = abs(sums - target)

                if sums < target:
                    r+=1
                else:
                    l-=1

        return closest_sum