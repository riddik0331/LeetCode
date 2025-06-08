# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     link_1 = set()
    #     link_2 = set()
    #     node_A = headA
    #     node_B = headB
    #     while node_A or node_B:
    #         if node_A:
    #             if (node_A, node_A.next) in link_2:
    #                 return node_A
    #             link_1.add((node_A, node_A.next))
    #             node_A = node_A.next
    #         if node_B:
    #             if (node_B, node_B.next) in link_1:
    #                 return node_B
    #             link_2.add((node_B, node_B.next))
    #             node_B = node_B.next


        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            link_1 = dict()
            link_2 = dict()
            node_A = headA
            node_B = headB
            while node_A or node_B:
                if node_A:
                    if (node_A, node_A.next) in link_2.items():
                        return node_A
                    link_1[node_A] = node_A.next
                    node_A = node_A.next
                if node_B:
                    if (node_B, node_B.next) in link_1.items():
                        return node_B
                    link_2[node_B] = node_B.next
                    node_B = node_B.next
