class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        while node1 and node2:
            if node1.val<node2.val and node1.next.val>=node2.val:
                tmp = node2.next
                node2.next = node1.next
                node1.next = node2
                node2 = tmp
                node1 = node1.next
            elif node2.val<node1.val and node2.next.val>=node1.val:
                tmp = node1.next
                node1.next = node2.next
                node2.next = node1
                node1 = tmp
                node2 = node2.next
            else:
                node1 = node1.next
                node2 = node2.next
        return l1 if l1.val<l2.val else l2

def createList(nums: list):
    head = ListNode(0)
    node = head
    for i in nums:
        node.next = ListNode(i)
        node = node.next

    return head.next

Solution().mergeTwoLists(createList([1, 2, 4]), createList([1, 3, 4]))
