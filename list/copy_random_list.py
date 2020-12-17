class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head: ListNode)->ListNode:
        if head is None:
            return head

        dic = {}
        cur = head
        while cur:
            dic[cur] = ListNode(cur.val)
            cur = cur.next

        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)

        return dic[head]
