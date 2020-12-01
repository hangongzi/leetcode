class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root):
        self.node_stack = []
        while root:
            self.node_stack.append(root)
            root = root.left

    def next(self):
        node = self.node_stack.pop()
        tmp = node.right
        while tmp:
            self.node_stack.append(tmp)
            tmp = tmp.left
        return node.val

    def hasNext(self):
        if not self.node_stack:
            return False
        return True


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

tree_obj = BSTIterator(root)


