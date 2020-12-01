class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for c in path.split('/'):
            if not c:
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            elif c != '.':
                stack.append(c)
        return '/'+'/'.join(stack)

print(Solution().simplifyPath('/../'))
