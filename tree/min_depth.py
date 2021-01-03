class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
from collections import deque
def min_depth(root: TreeNode):
    if not root:
        return 0
    # 迭代实现：BFS
    q = deque([root])
    depth = 1
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        depth += 1
    return depth
    # 递归实现
    # return 1+min(min_depth(root.left), min_depth(root.right))

root = TreeNode(3)
root.left = TreeNode(9)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(min_depth(root))
