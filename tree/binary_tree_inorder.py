class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def inorderTrace(self, root: TreeNode)->list:
        ret = list()
        self.helper(ret, root)
        return ret

    def helper(self, ret:list, root:TreeNode):
        if root is None:
            return
        self.helper(ret, root.left)
        ret.append(root.val)
        self.helper(ret, root.right)

    # 迭代版中序遍历
    def inorder(root: TreeNode):
        ans = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans

nums = [1,3,5,6,2,4]
def createBinaryTree(nums):
    if not nums:
        return None
    
    root = TreeNode(nums[0])
    nodeList = [root]
    front = 0
    index = 1

    while index<len(nums):
        node = nodeList[front]
        front += 1

        node.left = TreeNode(nums[index])
        nodeList.append(node.left)
        index += 1

        if index>=len(nums):
            break

        node.right = TreeNode(nums[index])
        nodeList.append(node.right)
        index += 1

    return root

tree = createBinaryTree(nums)
ret = Solution().inorderTrace(tree)
print(ret)