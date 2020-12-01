class Solution(object):
    def calculate(self, s):
        def help(s: list):
            stack = []
            num = 0
            flag = '+'

            while s:
                c = s.pop(0)
                if c.isdigit():
                    num = num*10+int(c)
                if c == '(':
                    num = help(s) # 目的就是将括号里的内容简化为一个数，因此放到生成数的位置
                elif (not c.isdigit() and c!=' ') or len(s)==0:
                    if flag == '+':
                        stack.append(num)
                    elif flag == '-':
                        stack.append(-num)
                    elif flag == '*':
                        stack.append(stack.pop()*num)
                    elif flag == '/':
                        stack.append(int(stack.pop()/float(num)))
                    
                    flag = '+' if c=='(' else c
                    num = 0
                    
                if c == ')': break
                    

            return sum(stack)
        return help(list(s))

print(Solution().calculate("2-(5-6)+(5-3)*6"))
        # stack = []
        # num = 0
        # flag = 1
        # res = 0
        # for c in s:
        #     if c == ' ':
        #         continue

        #     if c.isdigit():
        #         num = num*10+int(c)
        #     elif c == '+':
        #         res += flag*num
        #         flag = 1
        #         num = 0
        #     elif c == '-':
        #         res += flag*num
        #         num = 0
        #         flag = -1
        #     elif c == '(':
        #         stack.append(res)
        #         stack.append(flag)
        #         flag = 1
        #         res = 0
        #     elif c == ')':
        #         res += flag * num
        #         res *= stack.pop()
        #         res += stack.pop()
        #         num = 0
        # return res + flag*num


