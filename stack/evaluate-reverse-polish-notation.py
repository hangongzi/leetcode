class Solution(object):
    def evalRPN(self, tokens):
        def compute(n1, n2, flag):
            if flag=='+':
                return n1+n2
            elif flag == '-':
                return n1-n2
            elif flag == '*':
                return n1*n2
            else:
                if n1*n2<0:
                    return 0-(abs(n1)//abs(n2))
                return n1//n2
        ans = 0
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']: 
                if len(stack)>=2:
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(compute(n2, n1, i))
            else:
                stack.append(int(i))

        return stack[-1]

print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

