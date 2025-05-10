#Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:
# Input: head = [1,1,1,2,3]

#Time Complexity: O(n)
#Space Complexity: O(1)


from typing import Optional
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
        dummyNode = ListNode(0, head)
        prev = dummyNode
        flag = False
        
        while current_node!=None and current_node.next:
            if current_node.val == current_node.next.val:
                while current_node.next!=None and current_node.val == current_node.next.val:
                    current_node = current_node.next

                prev.next = current_node.next
            else:
                prev = prev.next
            current_node = current_node.next
        return dummyNode.next
        