class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.status = True
        self.pre_num = None
        def helper(root):
            if not root or self.status is False:
                return
            helper(root.left)
            if self.pre_num is not None and self.pre_num>=root.val:
                self.status = False
                return
            self.pre_num=root.val
            helper(root.right)

        helper(root)
        return self.status
        
root = TreeNode(1)
root.left = TreeNode(1)


Solution().isValidBST(root)