class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(preorder: list, inorder: list, preStart: int, inStart: int, inEnd: int):
    if preStart>=len(preorder) or inStart>inEnd:
        return None

    root = TreeNode(preorder[preStart])
    inIndex = 0
    for i in range(inStart, inEnd+1):
        if inorder[i] == preorder[preStart]:
            inIndex = i
            break
    root.left = build_tree(preorder, inorder, preStart+1, inStart, inIndex-1)
    root.right = build_tree(preorder, inorder, preStart+1, inIndex+1, inEnd)
    return root


# ret = build_tree()
