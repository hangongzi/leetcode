class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        flag = "+" # 记录前一个符号

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)
            if (not c.isdigit() and c != ' ') or i==len(s)-1:
                if flag == '+':
                    stack.append(num)
                elif flag == '-':
                    stack.append(-num)
                elif flag == '*':
                    stack.append(stack.pop()*num)
                elif flag == '/':
                    stack.append(int(stack.pop()/float(num)))
                flag = c
                num = 0

        return sum(stack)

print(Solution().calculate("14-3/2"))
