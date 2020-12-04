class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def createList(nums: list):
    head = ListNode(0)
    node = head
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

def printList(head: ListNode):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    print(ans)
