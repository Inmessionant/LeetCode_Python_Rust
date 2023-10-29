class BrowserHistorySys:
    def __init__(self, homepage: str, max_count: int):
        
        self.maxcount = max_count
        self.visited_page = [homepage]
        self.cur_page = homepage

    def visit(self, url: str) -> int:
        return 0

    def back(self) -> str:
        return ""

    def forward(self) -> str:
        return ""
