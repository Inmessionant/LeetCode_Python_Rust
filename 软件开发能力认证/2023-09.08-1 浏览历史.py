import collections


class BrowserHistorySys:
    def __init__(self, homepage: str, max_count: int):

        self.maxcount = max_count
        self.visited_page = collections.deque([homepage])
        self.cur_page = homepage

    def visit(self, url: str) -> int:

        if url == self.cur_page:
            ...
        else:
            while self.visited_page[-1] != self.cur_page:
                self.visited_page.pop()

            self.cur_page = url
            self.visited_page.append(self.cur_page)

        while len(self.visited_page) > self.maxcount:
            self.visited_page.popleft()

        return len(self.visited_page)

    def back(self) -> str:
        if self.visited_page[0] == self.cur_page:
            ...
        else:
            idx = self.visited_page.index(self.cur_page)
            self.cur_page = self.visited_page[idx - 1]

        return self.cur_page

    def forward(self) -> str:
        if self.visited_page[-1] == self.cur_page:
            ...
        else:
            idx = self.visited_page.index(self.cur_page)
            self.cur_page = self.visited_page[idx + 1]

        return self.cur_page


obj = BrowserHistorySys("w3.huawei.com", 10)
print(
    obj.visit("google.com"),
    obj.back(),
    obj.forward(),
    obj.forward(),
    obj.visit("baidu.com"),
    obj.visit("youtube.com"),
    obj.back(),
    obj.visit("baidu.com"),
    obj.back(),
    obj.visit("mails.huawei.com"))


obj = BrowserHistorySys("www.huawei.com", 3)
print(
    obj.visit("w3.huawei.com"),
    obj.visit("w4.huawei.com"),
    obj.back(),
    obj.visit("www.huawei.com"),
    obj.visit("w5.huawei.com"),
    obj.visit("w6.huawei.com"))
