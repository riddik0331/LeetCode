# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        res = ListNode(0)
        cur = res
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return res.next

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = head
    #     prev = None

    #     while curr:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     return prev
