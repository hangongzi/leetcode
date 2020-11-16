class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_balanced(root: TreeNode) -> bool:
    def balanced(root: TreeNode, height=0):
        if not root:
            height = 0
            return True, height
        balanc_left, left = balanced(root.left)
        balanc_right, right = balanced(root.right)

        if balanc_left and balanc_right:
            # 没有添加等于1的情况
            if abs(left - right) <= 1:
                height = left + 1 if left > right else right + 1
                return True, height
        return False, height

    balance, height = balanced(root, 0)
    return balance


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(7)
    is_balanced(root)
