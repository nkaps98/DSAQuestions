from typing import List

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. More formally, if there are multiple valid answers, you can return any of them.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the unique elements in the first k slots of nums.
# Custom test case:
# For example, given nums = [1,1,1,2,2,3], your solution should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. Note that the order of those five elements may be incorrect. It doesn't matter what values are set beyond the returned k (hence they are underscores).

# Brute force approach
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count_dict = {}
        while i != len(nums) and nums[i]!="_":
            decrement=False
            if nums[i] not in count_dict:
                count_dict[nums[i]] = 1
            else:
                count_dict[nums[i]] += 1

            if count_dict[nums[i]] > 2 and count_dict[nums[i]]!="_":
                decrement = True
                # print(i, nums[i])
                if i == len(nums)-1:
                    nums.pop()
                    break
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
                    nums[j+1] = '_'
                    
            if not decrement:
                i+=1
        
        count = 0
        for i in nums:
            if type(i) == int:
                count+=1
                
        return count
    

# Optimized approach
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        count=1
        j = 1
        while i <= len(nums)-1:
            if nums[i-1] == nums[i]:
                count+=1

            elif nums[i-1] != nums[i]:
                count=1

            if count <= 2:
                nums[j] = nums[i]
                j+=1
