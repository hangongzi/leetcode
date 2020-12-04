class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(head: ListNode):
            pre = head
            cur = head.next
            tmp = head.next.next

            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            head.next = None
            return pre

        head = ListNode(0)
        node = head
        inc = 0
        while l1 and l2:
            node.next = ListNode((l1.val+l2.val+inc)%10)
            inc = (l1.val+l2.val+inc)//10
            node = node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            node.next = ListNode((l1.val+inc)%10)
            node = node.next
            inc = (l1.val+inc)//10
            l1 = l1.next

        while l2:
            node.next = ListNode((l2.val+inc)%10)
            node = node.next
            inc = (l2.val+inc)//10
            l2 = l2.next
        if inc:
            node.next = ListNode(inc)

        return head.next


def createList(l: list):
    head = ListNode(0)
    node = head
    for i in l:
        node.next = ListNode(i)
        node = node.next
    return head.next


Solution().addTwoNumbers(createList([9,9,9,9,9,9,9]), createList([9,9,9,9]))
