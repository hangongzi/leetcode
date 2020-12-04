class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head: ListNode):
        if head is None or head.next is None:
            return head

        # 递归
        newpre = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newpre

        # 迭代法
        # pre = head
        # cur = head.next
        # tmp = head.next.next
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp

        # head.next = None

        # return pre

import list_method
list_method.printList(Solution().reverseList(list_method.createList([1,2,3,4])))
