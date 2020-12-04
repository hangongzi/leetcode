class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeTwo(l1: ListNode, l2: ListNode)->ListNode:
            prevhead = ListNode(-1)
            prev = prevhead
            while l1 and l2:
                if l1.val < l2.val:
                    prev = l1
                    l1 = l1.next
                else:
                    prev = l2
                    l2 = l2.next
            prev.next = l1 if l1 is not None else l2
            return prevhead.next

        def sort(head: ListNode, tail: ListNode)->ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return mergeTwo(sort(head, mid), sort(mid.next, tail))

        tail = head
        while tail.next is not None:
            tail = tail

        return sort(head, tail)

import list_method
list_method.printList(Solution().sortList(list_method.createList([2,1,5,3,4])))