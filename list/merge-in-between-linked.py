class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        pre_a, pre_b = None, None
        if a>0:
            b = b-a+1
            while a-1:
                node = node.next
                a -= 1
        pre_a = node
        pre_b = pre_a
        while b:
            pre_b = pre_b.next
            b -= 1

        end_l2 = list2
        while end_l2.next:
            end_l2 = end_l2.next

        del_nodes = pre_a
        if a == 0:
            end_l2.next = pre_b.next
            pre_b.next = list2
            return pre_b.next
        else:
            pre_a.next = list2
            end_l2.next = pre_b.next
        pre_b.next = None
        while del_nodes:
            del_node = del_nodes
            del_nodes = del_nodes.next
            del del_node

        return list1

from list_method import *

printList(Solution().mergeInBetween(createList([0,1,2,3,4,5,6]), 0, 6, createList([10000, 10001, 10002, 10003])))
