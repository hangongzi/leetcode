class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class FrontMiddleBackQueue:
    def __init__(self):
        self.head = Node(0)
        self.count = 0

    def pushFront(self, val: int) -> None:
        node = Node(val)
        if self.head.next is None:
            self.head.next = node
        else:
            node.next = self.head.next
            self.head.next = node
        self.count += 1

    def pushMiddle(self, val: int) -> None:
        c = (self.count)//2
        node = self.head
        while c:
            node = node.next
            c -= 1
        node_t = Node(val)
        node_t.next = node.next
        node.next = node_t
        self.count += 1

    def pushBack(self, val: int) -> None:
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)
        self.count += 1


    def popFront(self) -> int:
        if self.count == 0:
            return -1
        del_node = self.head.next
        self.head.next = del_node.next
        res = del_node.val
        del del_node
        self.count -= 1
        return res

    def popMiddle(self) -> int:
        if self.count == 0:
            return -1
        node = self.head
        c = (self.count-1)//2
        while c:
            node = node.next
            c -= 1
        del_node = node.next
        node.next = del_node.next
        res = del_node.val
        del del_node
        self.count -= 1
        return res


    def popBack(self) -> int:
        if self.count == 0:
            return -1

        node = self.head
        while node.next.next:
            node = node.next
        del_node = node.next
        res = del_node.val
        node.next = None
        del del_node
        self.count -= 1
        return res

obj = FrontMiddleBackQueue()

obj.pushFront(1)
obj.pushBack(2)
obj.pushMiddle(3)
obj.pushMiddle(4)
print(obj.popFront())
print(obj.popMiddle())
print(obj.popMiddle())
print(obj.popBack())
print(obj.popFront())

