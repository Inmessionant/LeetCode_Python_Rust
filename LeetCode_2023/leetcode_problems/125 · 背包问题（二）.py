class Solution:
    def back_pack_i_i(self, bagweight, weight, value):
        len_weight, len_bagweight = len(weight), bagweight
        dp = [0 for _ in range(len_bagweight + 1)]

        for i in range(len_weight):
            for j in range(len_bagweight, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

        return dp[-1]
    def back_pack_i_i(self, bagweight, weight, value):

        len_weight, len_bagweight = len(weight), bagweight
        dp = [[0 for _ in range(len_bagweight + 1)] for _ in range(len_weight)]

        for j in range(weight[0], len_bagweight + 1):
            dp[0][j] = value[0]

        for i in range(1, len_weight):
            for j in range(len_bagweight + 1):
                if j < weight[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

        return dp[-1][-1]


bagweight = 10
weight = [2, 3, 5, 7]
value = [1, 5, 2, 4]
print(Solution().back_pack_i_i(bagweight, weight, value))
