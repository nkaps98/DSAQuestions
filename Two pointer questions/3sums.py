from typing import List

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# The solution should be done in O(n^2) time complexity and O(1) space complexity.

# Approach:
# 1. Sort the array to make it easier to avoid duplicates.
# 2. Use a for loop to iterate through the array.
# 3. For each element, use two pointers (left and right) to find pairs that sum to the negative of the current element.
# 4. If the sum of the triplet is zero, add it to the result list.
# 5. Move the left pointer to the right and the right pointer to the left to find new pairs.
# 6. Skip duplicates by checking if the current element is the same as the previous one.
# 7. Continue until all triplets are found.
# 8. Return the list of unique triplets.
# Time Complexity: O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sum_pairs = []
        count = 0
        target = 0
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1

            if i > 0 and nums[i-1] == nums[i]:
                continue

            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums < target:
                    j+=1
                elif sums > target:
                    k-=1
                else:
                    sum_pairs.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1

                    while nums[j] == nums[j-1] and j<k:
                        j+=1

        return sum_pairs