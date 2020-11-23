class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 1
        node = head
        while node.next:
            length += 1
            node = node.next

        if length==n:
            return head.next
        
        node_idx = 1
        node = head
        while node_idx<length-n:
            node_idx+=1
            node = node.next

        if node_idx==1 and length==1:
            return None
        elif node_idx==1 and length==2:
            head.next = None
        else:
            del_node = node.next
            node.next = del_node.next
            del del_node

        return head



def createList(nums: list)->ListNode:
    head = ListNode(0)
    node = head
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next


ret = Solution().removeNthFromEnd(createList([1,2,3,4,5]), 1)