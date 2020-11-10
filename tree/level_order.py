from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        ret = list()
        if not root:
            return ret

        que = deque()
        que.append(root)
        while que:
            currentLevelSize = len(que)
            ret.append([])
            for i in range(1, currentLevelSize+1):
                node = que.popleft()
                ret[-1].append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)

        return ret


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().levelOrder(root))
