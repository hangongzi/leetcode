# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def sumNumbers(self, root:TreeNode)->int:
        if not root:
            return 0
        total = 0
        nodeQueue = deque([root])
        numQueue = deque([root.val])

        while nodeQueue:
            node = nodeQueue.popleft()
            num = numQueue.popleft()

            left, right = node.left, node.right
            if node.left is None and node.right is None:
                total += num
            else:
                if left:
                    nodeQueue.append(left)
                    numQueue.append(num*10+left.val)
                if right:
                    nodeQueue.append(right)
                    numQueue.append(num*10+right.val)
        return total


root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

ret = Solution().sumNumbers(root)
print(ret)
