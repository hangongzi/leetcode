class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        def build(l, r):
            mid = (l+r)//2
            o = TreeNode(nums[mid])
            if l<=mid-1:
                o.left = build(l, mid-1)
            if r>=mid+1:
                o.right = build(mid+1, r)
            return o
        
        nums = list()
        inorder(root)
        return build(0, len(nums)-1)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

ret = Solution().balanceBST(root)
print(ret)
