class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def midOrder(root: TreeNode):
    ans = []
    node_stack = []

    while root or node_stack:
        while root:
            node_stack.append(root)
            root = root.left
        root = node_stack.pop()
        ans.append(root.val)
        root = root.right
    
    return ans

root = TreeNode(1)
root.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(midOrder(root))
