class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 递归
        self.tmp = head
        def check(head):
            if head is None:
                return True
            ret = check(head.next) and (self.tmp.val==head.val)
            self.tmp = self.tmp.next
            return ret
        
        return check(head)
            
        # 翻转链表
        # slow = fast = head
        # while fast:
        #     slow = slow.next
        #     fast = fast.next
        #     if fast:
        #         fast = fast.next

        # head_mid = self.reverseList(slow)
        # while head_mid:
        #     if head.val != head_mid.val:
        #         break
        #     head = head.next
        #     head_mid = head_mid.next
        # if head_mid is not None:
        #     return False
        # return True

    def reverseList(self, head: ListNode)->ListNode:
        if head is None or head.next is None:
            return head

        newpre = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newpre


from list_method import *

print(Solution().isPalindrome(createList([1,0, 0])))

