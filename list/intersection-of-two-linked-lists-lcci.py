class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        t1, t2 = headA, headB
        while t1 != t2:
            if t1 is None:
                t1 = headB
            else:
                t1 = t1.next
            if t2 is None:
                t2 = headA
            else:
                t2 = t2.next
        return t1

from list_method import *
l1 = createList([4, 1, 8, 4, 5])
l2 = ListNode(5)
l2.next = ListNode(0)
l2.next.next = ListNode(1)
l2.next.next.next = l1.next.next

ret = Solution().getIntersectionNode(headA=l1, headB=l2)
print(ret.val)
