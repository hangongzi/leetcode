class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        hl, hr = 0, 0
        node = root
        while node:
            hl += 1
            node = node.left

        node = root
        while node:
            hr += 1
            node = node.right

        if hl == hr:
            return (1<<hl)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

print(Solution().countNodes(root))
