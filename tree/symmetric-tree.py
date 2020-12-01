from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def check(u, v):
            q = deque()
            q.append(u)
            q.append(v)
            while q:
                pre = q.popleft()
                pos = q.popleft()
                if not pre and not pos: continue
                if (not pre or not pos) or (pre.val != pos.val): return False
                q.append(pre.left)
                q.append(pos.right)
                q.append(pre.right)
                q.append(pos.left)
            return True
        return check(root, root)

        # 递归
        # def check(p, q):
        #     if not p and not q: return True
        #     if not p or not q: return False
        #     return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        # if not root:
        #     return True
        # return check(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))