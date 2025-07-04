# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack = {}
        while head:
            if head in stack:
                return True
            stack[head] = head.next
            head = head.next

        return False
            
