class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r, n = 0, 0, len(s)
        max_len = 0
        last_idx_dict = dict()

        while r < n:

            last_idx_dict[s[r]] = r

            if s[r] in last_idx_dict and last_idx_dict[s[r]] >= l:
                max_len = max(max_len, r - l)
                l = last_idx_dict[s[r]] + 1

            r += 1

        return max(max_len, r - l)


s = " "
print(Solution().lengthOfLongestSubstring(s))
