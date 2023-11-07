from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[0])
        arrows = [points[0]]

        for i in range(1, len(points)):
            if points[i][0] > arrows[-1][1]: # 气球i和气球i-1不挨着，注意这里不是>=
                arrows.append(points[i])
            else:
                # 两个气球重叠，需要更新当前一只箭可以引爆当前若干气球的边界
                arrows[-1][0], arrows[-1][1] = max(arrows[-1][0], points[i][0]), min(arrows[-1][1], points[i][1])

        return len(arrows)


points = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(Solution().findMinArrowShots(points))
