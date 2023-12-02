

class Solution:

    def display_pages(self, page_count: int, max_width: int, current_page: int) -> str:

        if page_count <= max_width:
            return ''.joon([str(i) for i in range(1, page_count + 1)])

        left_idx, right_idx = max_width // 2, page_count - (max_width // 2)

        if current_page <= left_idx:
            page_info = ''.join([str(i) for i in range(1, max_width - 1)])
            return "{}...{}".format(page_info, page_count)

        if current_page > right_idx:
            page_info = ''.join([str(i) for i in range(page_count - max_width + 3, page_count + 1)])
            return "1...{}".format(page_info)

        


obj = Solution()
print(Solution().display_pages(7, 6, 4))