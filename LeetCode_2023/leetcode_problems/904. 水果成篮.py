import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        l, r = 0, 0
        n = len(fruits)
        fruit_cnt = 0
        fruits_kinds = collections.defaultdict(int)
        max_len = 0

        while r < n:
            if fruits_kinds[fruits[r]] == 0:
                fruit_cnt += 1
            fruits_kinds[fruits[r]] += 1

            while fruit_cnt > 2:
                fruits_kinds[fruits[l]] -= 1
                if fruits_kinds[fruits[l]] == 0:
                    fruit_cnt -= 1
                l += 1

            max_len = max(r - l + 1, max_len)
            r += 1

        return max_len