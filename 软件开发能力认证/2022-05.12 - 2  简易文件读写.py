import sys


class File:
    def __init__(self, content, state, pos, read, write):
        self.content = content
        self.state = state
        self.pos = pos
        self.read = read
        self.write = write


class TextFileSys:

    def __init__(self):
        self.file_mgr = {}
        self.rule = {
            'r': [False, 'start', True, False],
            'r+': [False, 'start', True, True],
            'w': [True, 'end', False, True],
            'w+': [True, 'end', True, True],
            'a': [False, 'end', False, True],
            'a+': [False, 'end', True, True]
        }

    def open(self, filename: str, mode: str) -> int:
        if filename in self.file_mgr:
            cur_file = self.file_mgr.get(filename)
            if not cur_file.state:
                if self.rule[mode][0]:  cur_file.content = ""  # 打开时需要判断是否清空内容
                cur_file.state = True
                cur_file.pos = 0 if self.rule[mode][1] == 'start' else len(cur_file.content)
                cur_file.read, cur_file.write = self.rule[mode][2], self.rule[mode][3]

                return 0
            else:
                return -1
        else:
            if mode == 'r' or mode == 'r+':
                return -1
            else:
                content, pos = "", 0
                readble, writeable = self.rule[mode][2], self.rule[mode][3]
                self.file_mgr[filename] = File(content, True, pos, readble, writeable)
                return 0

    def close(self, filename: str) -> int:
        if self.file_mgr[filename].state:
            self.file_mgr[filename].state = False
            return 0
        else:
            return -1

    def write(self, filename: str, content: str) -> int:
        cur_file = self.file_mgr.get(filename)
        if cur_file and cur_file.state and cur_file.write:
            cur_str = cur_file.content[:cur_file.pos] + content
            len_cur_str = len(cur_str)
            cur_file.content = cur_str
            cur_file.pos = len_cur_str
            return len_cur_str

        else:
            return -1

    def read_all(self, filename: str) -> str:
        cur_file = self.file_mgr.get(filename)
        if cur_file and cur_file.read:
            return "null" if cur_file.content == '' else cur_file.content
        else:
            return "error"


# obj = TextFileSys()
# print(obj.open("file1", "w"))
# print(obj.open("file2", "a"))
# print(obj.write("file1", "engineer"))
# print(obj.close("file1"))
# print(obj.read_all("file1"))
# print(obj.read_all("file2"))

obj = TextFileSys()
print("2: ", obj.open("f", "a"))
print("3: ", obj.write("f", "hello"))
print("4: ", obj.close("f"))
print("5: ", obj.open("f", "w+"))
print("6: ", obj.read_all("f"))
print("7: ", obj.write("f", "how"))
print("8: ", obj.close("f"))
print("9: ", obj.open("f", "a+"))
print("10: ", obj.write("f", "areyou"))
print("11: ", obj.read_all("f"))
