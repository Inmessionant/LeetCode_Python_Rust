'''
现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。您有一个单词列表（从词典中获得的），该单词列表内的单词已经按这门新语言的字母顺序进行了排序。需要根据这个输入的列表，还原出此语言中已知的字母顺序。

示例 1：
输入:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
输出: "wertf"
'''

import collections
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        if not words: return ''

        if len(words) == 1: return words[0]

        graph_neighbor = collections.defaultdict(list)
        in_dgree = {char: 0 for word in words for char in word}

        for pair in zip(words[:-1], words[1:]):
            # pair = ('wrt', 'wrf')
            # *pair = wrt wrf
            # x, y = w w, r r, t f
            for x, y in zip(*pair):
                if x != y:
                    graph_neighbor[x].append(y)
                    in_dgree[y] += 1

        res = []
        queue = collections.deque()

        for i in in_dgree:
            if in_dgree[i] == 0:
                queue.append(i)

        while queue:
            cur_node = queue.popleft()
            res.append(cur_node)
            for neighbor_node in graph_neighbor[cur_node]:
                in_dgree[neighbor_node] -= 1
                if in_dgree[neighbor_node] == 0:
                    queue.append(neighbor_node)

        return ''.join(res) if len(res) == len(in_dgree) else ''


s = Solution()
print(s.alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]))
