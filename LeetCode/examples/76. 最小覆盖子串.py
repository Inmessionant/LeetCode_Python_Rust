import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, n = 0, 0, len(s)
        min_str, min_len = "", float("inf")
        need_map, need_cnt = collections.defaultdict(int), len(t)

        for char in t:
            need_map[char] += 1

        while r < n:
            if need_map[s[r]] > 0:
                need_cnt -= 1
            need_map[s[r]] -= 1

            while need_cnt == 0:
                cur_len = r - l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    min_str = s[l: r + 1]

                if need_map[s[l]] == 0:
                    need_cnt += 1
                need_map[s[l]] += 1
                l += 1

            r += 1

        return min_str


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
