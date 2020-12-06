class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 快排思想
        p = ListNode(-1)
        p.next = head
        ans = p
        while head:
            if head.val<x:
                p = p.next
                p.val, head.val = head.val, p.val
            head = head.next

        return ans.next

        # 双指针
        # if head is None or head.next is None:
        #     return head

        # p1 = ListNode(-1)
        # p2 = ListNode(-1)
        # head1, head2 = p1, p2

        # while head:
        #     next_node = head.next
        #     if head.val<x:
        #         p1.next = head
        #         p1 = p1.next
        #     else:
        #         p2.next = head
        #         p2 = p2.next
        #     head.next = None
        #     head = next_node

        # p1.next = head2.next
        # return head1.next

from list_method import *

printList(Solution().partition(createList([3, 5, 8, 5, 10, 2, 1]), 5))