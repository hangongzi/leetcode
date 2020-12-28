def post_order(root: TreeNode):
    ans = []
    stack = []
    pre = None
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        if root.right is None or root.right == pre:
            ans.append(root.val)
            pre = root
            root = None
        else:
            stack.append(root)
            root = root.right
        

    return ans
    