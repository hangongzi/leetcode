class Solution:
    def reconstructQueue(self, people: list):
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            space = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    space -= 1
                    if space == 0:
                        ans[i] = person
                        break
        return ans


print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
