from typing import (
    List,
)

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        # Write your code here
        nums.sort()
        count = 0
        for i in range(0, len(nums)-1):
            l = i+1
            r = len(nums)-1

            while l < r and r <= len(nums)-1:
                current_sums = nums[i] + nums[l] + nums[r]
                if current_sums < target:
                    count += r - l
                    l += 1
                
                else:
                    r -= 1
        
        return count
