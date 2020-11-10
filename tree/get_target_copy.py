import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.result = None
        self.flag = True
        def helper(root, target):
            if not root:
                return
            if root.val == target.val:
                checkValid(root, target)
                if self.flag:
                    self.result = root
                    return
                else:
                    self.flag = True
            helper(root.left, target)
            helper(root.right, target)

        def checkValid(result, target):
            if not result:
                return
            if result.val != target.val or not target:
                self.flag = False
                return
            checkValid(result.left, target.left)
            checkValid(result.right, target.right)

        helper(original, target)

        return self.result


original = TreeNode(7)
original.left = TreeNode(3)
original.left.right = TreeNode(9)
original.right = TreeNode(3)
original.right.left = TreeNode(6)
original.right.right = TreeNode(19)

clone = copy.deepcopy(original)
Solution().getTargetCopy(original, clone, original.right)

