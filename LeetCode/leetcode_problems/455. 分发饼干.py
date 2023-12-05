from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 这里的局部最优就是大饼干喂给胃口大的，充分利用饼干尺寸喂饱一个，全局最优就是喂饱尽可能多的小孩
        if not s: return 0

        g.sort(reverse=True)
        s.sort(reverse=True)

        res = 0
        cookie_idx = 0

        for i in range(len(g)):
            if cookie_idx < len(s) and s[cookie_idx] >= g[i]:
                res += 1
                cookie_idx += 1

        return res


g = [1, 2, 3]
s = [1, 2]
print(Solution().findContentChildren(g, s))
