class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        # 迭代
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        l = l-k
        node = head
        while l:
            node = node.next
            l -= 1

        return node.val
        # 递归
        # self.count = 0
        # self.ans = None
        # def help(head):
        #     if head is None:
        #         return
        #     help(head.next)
        #     self.count += 1
        #     if self.count == k:
        #         self.ans = head.val
            
        # help(head)
        # return self.ans


from list_method import *

print(Solution().kthToLast(createList([1,2,3,4,5]), 2))
