from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        ans = []
        def dfs(node, level):
            if level>=len(ans):
                ans.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    ans[level].append(node.val)
                else:
                    ans[level].appendleft(node.val)
            for node_next in [node.left, node.right]:
                if node_next:
                    dfs(node_next, level+1)
        dfs(root, 0)
        return ans

        # ans = []
        # level_list = deque()
        # flag_level_left = True

        # node_queue = deque([root, None])

        # while len(node_queue)>0:
        #     cur_node = node_queue.popleft()
        #     if cur_node:
        #         if flag_level_left:
        #             level_list.append(cur_node.val)
        #         else:
        #             level_list.appendleft(cur_node.val)
        #         if cur_node.left:
        #             node_queue.append(cur_node.left)
        #         if cur_node.right:
        #             node_queue.append(cur_node.right)
        #     else:
        #         ans.append(list(level_list))
        #         if len(node_queue)>0:
        #             node_queue.append(None)
        #         level_list = deque()
        #         flag_level_left = not flag_level_left
        # return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().zigzagLevelOrder(root))
