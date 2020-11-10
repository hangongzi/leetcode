class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node):
        if not root:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if not root.children:
                continue
            stack.extend(root.children[::-1])
        return output

        # 递归法
        # if not root:
        #     return
        # self.nums = []
        # def helper(root):
        #     if not root:
        #         return
        #     self.nums.append(root.val)
        #     if not root.children:
        #         return
        #     for node in root.children:
        #         helper(node)
        # helper(root)
        # return self.nums

root = Node(val=1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])

Solution().preorder(root)