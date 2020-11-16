# 取中间数值为根节点，左侧为左子树，右侧为右子树
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def sortedArrToBST(self, arr: list):
        if not arr:
            return None
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.sortedArrToBST(arr[:mid])
        root.right = self.sortedArrToBST(arr[mid+1:])
        return root


ret = Solution().sortedArrToBST([1, 2, 3, 4, 5])
