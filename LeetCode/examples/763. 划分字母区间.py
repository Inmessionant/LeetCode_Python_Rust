from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_idx = dict()

        for idx, st in enumerate(s): # 存储每个字符最晚出现的idx
            last_idx[st] = idx

        left, right = 0, 0
        res = []

        for idx, st in enumerate(s):
            right = max(right, last_idx[st])  # 更新当前字符串片段中字符最晚出现的idx
            if right == idx:
                res.append(right - left + 1)
                left = right + 1

        return res


s = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(s))
