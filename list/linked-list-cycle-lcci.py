class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# m: 环外长度，n:环长度，y：环内相对位置
# m = n-y+(x-1)*n
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                break
        if fast != slow:
            return None

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
        

from list_method import *
l = createList([3, 2, 0, -4])
tail = l
while tail.next:
    tail = tail.next
tail.next = l.next

ret = Solution().detectCycle(l)
print(ret.val)