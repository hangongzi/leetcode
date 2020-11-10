class Solution:
    def generateParenthesis(self, n: int) -> list:
        self.ret = list()
        def generate(left, right, n, s):
            if left==n and right==n:
                self.ret.append(s)
                return
            if left<n: 
                generate(left+1, right, n, s+'(')
            if right<left: 
                generate(left, right+1, n, s+')')
            

        generate(0, 0, n, '')
        return self.ret

print(Solution().generateParenthesis(3))
