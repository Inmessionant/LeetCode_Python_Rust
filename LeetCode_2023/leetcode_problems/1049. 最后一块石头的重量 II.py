from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        target = sum(stones) // 2
        dp = [0 for _ in range(target + 1)]

        for i in range(len(stones)):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        return abs(sum(stones) - dp[-1] - dp[-1])


stones = [2, 7, 4, 1, 8, 1]
print(Solution().lastStoneWeightII(stones))
