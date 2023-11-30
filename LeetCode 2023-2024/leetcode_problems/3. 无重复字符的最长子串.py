class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r, n = 0, 0, len(s)
        max_len = 0
        last_idx = dict()

        while r < n:
            if s[r] in last_idx and last_idx[s[r]] >= l:  # 不满足条件
                max_len = max(max_len, r - l)
                l = last_idx[s[r]] + 1

            last_idx[s[r]] = r
            r += 1

        return max(max_len, r - l)  # 当s=“ ”，


s = " "
print(Solution().lengthOfLongestSubstring(s))
