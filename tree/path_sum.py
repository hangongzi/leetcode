class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int)->int:
        if root is None:
            return 0
        return self.dfs(root, target)+self.pathSum(root.left, target)+self.pathSum(root.right, target)

    def dfs(self, root: TreeNode, sum: int)->int:
        if root is None:
            return 0
        sum -= root.val
        return (1 if sum == 0 else 0) + self.dfs(root.left, sum) + self.dfs(root.right, sum)



root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(Solution().pathSum(root, 22))
