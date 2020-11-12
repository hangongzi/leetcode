# 斐波那契查找
# 树表查找
# 二叉查找树
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self, nums: list):
        self.root = TreeNode(nums[0])
        for i in nums[1:]:
            self.insert(i)

    def search(self, node: TreeNode, parent: TreeNode, val: int)->(bool, TreeNode, TreeNode):
        if node is None:
            return False, node, parent
        if node.val == val:
            return True, node, parent

        if node.val<val:
            return self.search(node.right, node, val)
        if node.val>val:
            return self.search(node.left, node, val)
        

    def insert(self, val):
        flag, node, parent = self.search(self.root, self.root, val)
        if flag is True:
            return
        if parent.val>val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

    def delete(self, val):
        flag, node, parent = self.search(self.root, self.root, val)
        if flag is False:
            return
        if node.left is None:
            if node == parent.left:
                parent.left = node.right
            else:
                parent.right = node.right
            del node
        elif node.right is None:
            if node == parent.left:
                parent.left = node.left
            else:
                parent.right = node.left
            del node
        else:
            pre = node.right
            if pre.left is None:
                node.val = pre.val
                node.right = pre.right
                del pre
            else:
                next_ = pre.left
                while next_.left is not None:
                    pre = next_
                    next_ = next_.left
                node.data = next_.val
                pre.left = next_.left
                del node

# 平衡查找树：2-3树
# 平衡查找树：红黑树
# B树和B+树
# 分块查找
# 哈希查找
# 参考链接: https://www.cnblogs.com/maybe2030/p/4715035.html

