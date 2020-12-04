class ListNone:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseList(l):
    if l is None or l.next is None:
        return l
    
    pre = l
    cur = l.next
    tmp = l.next.next
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    l.next = None
    return pre

    # 递归
    # newhead = reverseList(l.next)
    # l.next.next = l
    # l.next = None
    # return newhead
        

def sumOflistNum(l1, l2):
    l1 = reverseList(l1)
    l2 = reverseList(l2)

    head = ListNone(0)
    ret = head
    inc = 0
    while l1 and l2:
        ret.next = ListNone((l1.val+l2.val+inc)%10)
        inc = (l1.val+l2.val+inc)//10
        l1 = l1.next
        l2 = l2.next
        ret = ret.next

    while l1:
        ret.next = ListNone((l1.val+inc)%10)
        inc = (l1.val+inc)//10
        ret = ret.next
        l1 = l1.next
    while l2:
        ret.next = ListNone((l2.val+inc)%10)
        inc = (l2.val + inc)//10
        ret = ret.next
        l2 = l2.next

    if inc:
        ret.next = ListNone(inc)
    return reverseList(head.next)

def createList(nums: list):
    head = ListNone(0)
    node = head
    for i in nums:
        node.next = ListNone(i)
        node = node.next
    return head.next

def printListNum(l: ListNone):
    n = 0
    while l:
        n = n*10+l.val
        l = l.next

    print(n)

ret = sumOflistNum(createList([9, 3, 6]), createList([6, 4]))
printListNum(ret)
