class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        

def printList(root:ListNode):
    while root:
        print(root.val)
        root = root.next

def createList(nums: list):
    node = ListNode(nums[0])
    head = node
    for n in nums[1:]:
        node.next = ListNode(n)
        node = node.next

    return head

Solution().deleteNode(createList([4, 5, 1, 9]))
