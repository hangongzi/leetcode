import copy

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root2 = copy.deepcopy(root)
root2.left.val = 1
print(Solution().isSameTree(root, root2))
