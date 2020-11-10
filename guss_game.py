class Solution:
    def game(self, guess, answer) -> int:
        return len(list(filter(lambda x: x[0]==x[1], zip(guess, answer))))

print(Solution().game([2,2,3], [3,2,1]))
