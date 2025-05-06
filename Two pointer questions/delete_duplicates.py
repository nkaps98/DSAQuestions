"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:  
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current_node = head
        next_node = head.next
        
        while next_node:
            if current_node.val == next_node.val:
                current_node.next = next_node.next
                if current_node:
                    next_node = current_node.next
                else:
                    break
            else:
                current_node = current_node.next
                next_node = next_node.next
        return head