class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        inc = 0
        ans = ListNode(0)
        node = ans
        while l1 and l2:
            node.next = ListNode((l1.val+l2.val+inc)%10)
            inc = (l1.val+l2.val+inc)//10
            node = node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            node.next = ListNode((l1.val+inc)%10)
            inc = (l1.val+inc)//10
            node = node.next
            l1 = l1.next

        while l2:
            node.next = ListNode((l2.val+inc)%10)
            inc = (l2.val+inc)//10
            node = node.next
            l2 = l2.next

        if inc:
            node.next = ListNode(inc)

        return ans.next


from list_method import *

printList(Solution().addTwoNumbers(createList([6, 1, 7]), createList([2, 9, 5])))
