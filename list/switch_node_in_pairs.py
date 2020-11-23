class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        p1, p2 = head, head.next
        p1.next = self.swapPairs(p2.next)
        p2.next = p1
        return p2

def createList(nums: list):
    head = ListNode(0)
    node = head
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

def printList(l: ListNode):
    while l:
        print(l.val)
        l = l.next


ret = Solution().swapPairs(createList([1,2,3,4]))
print(printList(ret))
