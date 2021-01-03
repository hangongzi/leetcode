class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        min_, max_, = float('-inf'), float('inf')
        def dfs(root: TreeNode):
            if not root:
                return max_, min_, 0
            lmin, lmax, lsum = dfs(root.left)
            rmin, rmax, rsum = dfs(root.right)
            if lmax<root.val<rmin:
                nonlocal res
                res = max(res, root.val+lsum+rsum)
                return min(lmin, root.val), max(rmax, root.val), root.val+lsum+rsum
            return min_, max_, 0
        res = 0
        dfs(root)
        return res


root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)
root.right.right.left = TreeNode(4)

print(Solution().maxSumBST(root))
            