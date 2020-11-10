class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min_diff, self.pre_num = -1, -1
        def helper(root: TreeNode):
            if root is None:
                return
            helper(root.left)
            if self.pre_num != -1:
                if self.min_diff != -1:
                    self.min_diff = min(root.val-self.pre_num, self.min_diff)
                else:
                    self.min_diff = root.val-self.pre_num
            self.pre_num = root.val
            helper(root.right)

        helper(root)
        return self.min_diff

    


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(7)

Solution().getMinimumDifference(root)