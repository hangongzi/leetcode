class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dumpHead = ListNode(0)
        dumpHead.next = head
        lastSorted = head
        cur = head.next
        while cur:
            if lastSorted.val<=cur.val:
                lastSorted = lastSorted.next
            else:
                prev = dumpHead
                while prev.next.val<=cur.val:
                    prev = prev.next
                lastSorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = lastSorted.next
        return dumpHead.next


from list_method import *

printList(Solution().insertionSortList(createList([4, 2, 1, 3])))
