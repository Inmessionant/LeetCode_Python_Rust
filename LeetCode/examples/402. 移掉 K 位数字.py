class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        remain = len(num) - k  # 移除k位，保留remain位

        for p in num:
            while k and stack and stack[-1] > p:  # 单调递增栈
                stack.pop()
                k -= 1

            stack.append(p)

        return ''.join(stack[:remain]).lstrip('0') or "0"


num = "1432219"
k = 3
print(Solution().removeKdigits(num, k))