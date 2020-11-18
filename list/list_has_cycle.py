class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        p1 = head
        p2 = head
        while p1 and p2 and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False


# l = ListNode(3)
# l.next = ListNode(2)
# l.next.next = ListNode(0)
# l.next.next.next = ListNode(-4)
# l.next.next.next.next = l.next
l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = l

print(Solution().hasCycle(l))