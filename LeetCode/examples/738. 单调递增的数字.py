class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:

        s = list(str(n))

        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) < int(s[i - 1]): # 前一个数字比当前数字大，前一个数字-1，当前位置到之后都设置为9
                s[i - 1] = str(int(s[i - 1]) - 1)
                s[i:] = '9' * (len(s) - i)

        return int("".join(s))


n = 1234
print(Solution().monotoneIncreasingDigits(n))
