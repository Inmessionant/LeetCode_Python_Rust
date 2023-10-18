import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def backtrack(start):

            if len(path) == len(tickets) + 1:
                res.append(path.copy())
                return True

            tickets_dict[start].sort()  # 可以保证字典序最小

            for _ in tickets_dict[start]:
                cur_to = tickets_dict[start].pop(0)
                path.append(cur_to)
                # 这里需要找下一个可用的地点，以前模板是一个list，需要从里面选择，
                # 此题用tickets_dict存储下一个地点，因此是backtrack(cur_to)
                if backtrack(cur_to):  # 只要找到一个解就返回，相当于剪枝
                    return True
                path.pop()
                tickets_dict[start].append(cur_to)

        '''
         {'JFK': ['SFO', 'ATL'], 
          'SFO': ['ATL'], 
          'ATL': ['JFK', 'SFO']}
        '''
        tickets_dict = collections.defaultdict(list)
        for start, end in tickets:
            tickets_dict[start].append(end)

        path, res = ['JFK'], []
        backtrack('JFK')

        return res[0]


tickets = [["MUC", "LHR"],
           ["JFK", "MUC"],
           ["SFO", "SJC"],
           ["LHR", "SFO"]]
print(Solution().findItinerary(tickets))
