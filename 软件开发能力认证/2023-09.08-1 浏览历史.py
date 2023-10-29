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


obj1 = BrowserHistorySys("w3.huawei.com", 10)
print(
    obj1.visit("google.com"),
    obj1.back(),
    obj1.forward(),
    obj1.forward(),
    obj1.visit("baidu.com"),
    obj1.visit("youtube.com"),
    obj1.back(),
    obj1.visit("baidu.com"),
    obj1.back(),
    obj1.visit("mails.huawei.com"))

obj2 = BrowserHistorySys("www.huawei.com", 3)
print(
    obj2.visit("w3.huawei.com"),
    obj2.visit("w4.huawei.com"),
    obj2.back(),
    obj2.visit("www.huawei.com"),
    obj2.visit("w5.huawei.com"),
    obj2.visit("w6.huawei.com"))
