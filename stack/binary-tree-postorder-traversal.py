class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        stack = []
        ans = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                ans.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return ans

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(Solution().postorderTraversal(root))
