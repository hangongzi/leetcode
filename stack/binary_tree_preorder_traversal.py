class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preOrder(root: TreeNode):
    ans = []
    node_stack = []

    while root or node_stack:
        while root:
            ans.append(root.val)
            node_stack.append(root)
            root = root.left
        
        while root is None and node_stack:
            root = node_stack.pop().right
        
    return ans


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(preOrder(root))
