class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        # 栈
        stack = []
        ans = []
        while root or len(stack)>0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans
        print(ans)

        # 递归
        # def help(root):
        #     if not root:
        #         return
        #     help(root.left)
        #     ret.append(root.val)
        #     help(root.right)

        # ret = []
        # help(root)
        # return ret


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)

ret = Solution().inorderTraversal(root)

