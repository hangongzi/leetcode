class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
         
    
print(Solution().defangIPaddr('1.1.1.1'))
# print('1.1.1.1'.replace('.', '[,]'))