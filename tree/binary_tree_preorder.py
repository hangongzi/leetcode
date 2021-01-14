class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.num = []
        def helper(root):
            self.num.append(root.val)
            helper(root.left)
            helper(right)
        helper(root)
        return self.num
        
    def pre_order(root: TreeNode):
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                ans.append(root.val)
                root = root.left
            while root is None and stack:
                root = stack.pop().right

    return ans




