# Brute Force

# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in nums:
            if i < k:
                count+=1
        
        l = 0
        r = 1
        prod = nums[l]
        while l < r and r <= len(nums)-1:
            prod *= nums[r]
            
            if prod < k:
                count += 1
            else:
                l += 1
                r = l + 1
                prod = nums[l]
                continue

            if r == len(nums) - 1:
                l += 1
                r = l + 1
                prod = nums[l]
            else:
                r += 1
        
        return count
        

# Time Complexity: O(n)
# Space Complexity: O(1)
# Optimal solution
# Approach:
# 1. Initialize two pointers, left and right, both starting at the beginning of the array.
# 2. Use a variable to keep track of the product of the elements between the two pointers.  
# 3. Iterate through the array with the right pointer, multiplying the product by the current element.
# 4. If the product is greater than or equal to k, move the left pointer to the right until the product is less than k.
# 5. For each position of the right pointer, add the number of valid subarrays ending at that position to the count.
# 6. The number of valid subarrays ending at the right pointer is equal to (right - left + 1).
# 7. Return the total count of valid subarrays.
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        l = 0
        prod = 1

        for r in range(len(nums)):
            prod *= nums[r]

            while prod >=k and l <= r:
                prod /= nums[l]
                l += 1
            count += r - l + 1
        
        return count