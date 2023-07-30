
class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 0, x

        while l <= r:
            mid = l + (r - l) // 2
            mid_pow = mid ** 2

            if mid_pow == x:
                return mid
            elif mid_pow < x:
                l = mid + 1
            else:
                r = mid - 1
        return r

x = 8
solution = Solution()
print(solution.mySqrt(x))
