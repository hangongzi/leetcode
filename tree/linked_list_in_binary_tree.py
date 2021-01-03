class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head, root):
            if head is None: return True
            if root is None or head.val != root.val: return False
            return dfs(head.next, root.left) or dfs(head.next, root.right)

        if root is None: return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)



root = TreeNode(1)
root.left = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.left.right.left = TreeNode(1)
root.right.left.right.right = TreeNode(3)

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(8)

print(Solution().isSubPath(head=head, root=root))
