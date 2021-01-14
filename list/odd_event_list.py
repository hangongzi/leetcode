# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        i = 0
        odd_h = ListNode(0)
        odd_l = odd_h
        event_h = ListNode(0)
        event_l = event_h
        node = head
        while node:
            if i % 2:
                odd_l.next = node # ListNode(node.val)
                odd_l = odd_l.next
            else:
                event_l.next = node # ListNode(node.val)
                event_l = event_l.next
            node = node.next
            i += 1
        
        event_l.next = odd_h.next
        odd_l.next = None
        return event_h.next


from list_method import *


if __name__ == '__main__':
    ret = Solution().oddEvenList(createList([1,2,3,4,5]))
    printList(ret)
