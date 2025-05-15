from typing import List

# Floyd's Tortoise and Hare (Cycle Detection) algorithm
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in an array using Floyd's Tortoise and Hare (Cycle Detection) algorithm.
        
        The array contains n + 1 integers, where each integer is in the range [1, n] inclusive.
        There is only one repeated number, which could be repeated more than once.
        
        This algorithm detects the duplicate without modifying the array and using only constant extra space.
        
        Explanation:
        - Treat the array like a linked list where the value at each index is the next pointer.
        - Since there is one duplicate, this forms a cycle.
        - Floyd's algorithm is used to detect the cycle and find the entry point (duplicate number).

        Args:
            nums (List[int]): A list of integers containing n + 1 elements with one duplicate.
        
        Returns:
            int: The duplicated integer in the list.
        """

        # Phase 1: Detect intersection point inside the cycle
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]         # Move one step
            fast = nums[nums[fast]]   # Move two steps
            if slow == fast:
                break                 # Cycle detected

        # Phase 2: Find entrance to the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
