from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res, l, r, n = [], 0, len(p) - 1, len(s)
        counter_s, counter_p = Counter(s[l: r]), Counter(p)

        while r < n:

            if not counter_s[s[r]]: counter_s[s[r]] = 0
            counter_s[s[r]] += 1

            if counter_s == counter_p:
                res.append(l)

            counter_s[s[l]] -= 1
            if counter_s[s[l]] == 0:
                del counter_s[s[l]]

            l += 1
            r += 1

        return res

s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
