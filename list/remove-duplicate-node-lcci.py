from list_method import *


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        nodes = set()
        node = head
        nodes.add(head.val)

        while node.next:
            cur = node.next
            if cur.val not in nodes:
                nodes.add(cur.val)
                node = node.next
            else:
                node.next = node.next.next

        node.next = None
        return head

printList(Solution().removeDuplicateNodes(createList([1,2,3,3,2,1])))
