# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        stack = list()
        result = []
        stack.append(root)
        node_l = None
        while stack or node_l:
            result.extend(list(map(lambda node: node.val, stack)))
            result.append('#')
            while stack:
                node_l = stack.pop()
            while node_l:
                if node_l.left:
                    if stack:
                        stack[-1].next = node_l.left
                    stack.append(node_l.left)
                if node_l.right:
                    if stack:
                        stack[-1].next = node_l.right
                    stack.append(node_l.right)
                if node_l.left is None or node_l.right is None:
                    node_l = None
                    break
                node_l = node_l.next

        return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

ret = Solution().connect(root)
print(ret)