class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        def mergeTwoList(l1: ListNode, l2: ListNode)->ListNode:
            prevhead = ListNode(-1)
            temp, temp1, temp2 = prevhead, l1, l2

            while temp1 and temp2:
                if temp1.val < temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            temp.next = temp1 if temp1 else temp2
            return prevhead.next

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        l1 = lists[0]
        for l2 in lists[1:]:
            l1 = mergeTwoList(l1, l2)

        return l1


def createList(nums: list):
    head = ListNode(0)
    node = head
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

def createLists(arrs: list):
    ans = []
    for arr in arrs:
        ans.append(createList(arr))
    return ans

Solution().mergeKLists(createLists([[1,4,5],[1,3,4],[2,6]]))