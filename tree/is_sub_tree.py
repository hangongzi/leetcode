class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def valid(t1: TreeNode, t2: TreeNode):
            if t2 is None: return True
            if t1 is None or (t1.val != t2.val): return False
            return valid(t1.left, t2.left) and valid(t1.right, t2.right)
        if t1 is None: return False
        return valid(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

t1 = TreeNode(1)
t1.right = TreeNode(2)
t1.right.left = TreeNode(4)

t2 = TreeNode(4)
t2.left = TreeNode(3)

print(Solution().checkSubTree(t1, t2))