class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        def generateTree(start, end):
            if start>end:
                return [None, ]

            allTrees = []
            for i in range(start, end+1):
                leftTrees = generateTree(start, i-1)
                rightTrees = generateTree(i+1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        curTree = TreeNode(i)
                        curTree.left = l
                        curTree.right = r
                        allTrees.append(curTree)

            return allTrees

        return generateTree(1, n) if n else []



