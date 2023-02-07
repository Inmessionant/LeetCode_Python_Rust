------



### 参考引用



- [x] Algorithm-Pattern：https://github.com/greyireland/algorithm-pattern
- [x] 代码随想录：https://programmercarl.com/



------



### Regex

- Guide：https://github.com/ziishaned/learn-regex/blob/master/translations/README-cn.md
- 练习网站：https://regex101.com/



**？的几种用法：**

- “?”元字符规定其前导对象必须在目标对象中连续出现零次或一次，如：abc(d)?可匹配abc和abcd；
- 当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的，非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配所有“o”；源字符串`str=“dxxddxxd”`中，`d\w*?`会匹配 dx,而`d\w*?d`会匹配 dxxd；



| 元字符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| .      | 句号匹配任意单个字符除了换行符。                             |
| [ ]    | 字符种类。匹配方括号内的任意字符。                           |
| [^ ]   | 否定的字符种类。匹配除了方括号里的任意字符                   |
| *      | 匹配>=0个重复的在*号之前的字符。                             |
| +      | 匹配>=1个重复的+号前的字符。                                 |
| ?      | 标记?之前的字符为可选.                                       |
| {n,m}  | 匹配num个大括号之前的字符或字符集 (n <= num <= m).           |
| (xyz)  | 字符集，匹配与 xyz 完全相等的字符串.                         |
| \|     | 或运算符，匹配符号前或后的字符.                              |
| \      | 转义字符,用于匹配一些保留的字符 `[ ] ( ) { } . * + ? ^ $ \ |` |
| ^      | 从开始行开始匹配.                                            |
| $      | 从末端开始匹配.                                              |



正则表达式提供一些常用的字符集简写。如下:

| 简写 | 描述                                               |
| ---- | -------------------------------------------------- |
| .    | 除换行符外的所有字符                               |
| \w   | 匹配所有字母数字，等同于 `[a-zA-Z0-9_]`            |
| \W   | 匹配所有非字母数字，即符号，等同于： `[^\w]`       |
| \d   | 匹配数字： `[0-9]`                                 |
| \D   | 匹配非数字： `[^\d]`                               |
| \s   | 匹配所有空格字符，等同于： `[\t\n\f\r\p{Z}]`       |
| \S   | 匹配所有非空格字符： `[^\s]`                       |
| \f   | 匹配一个换页符                                     |
| \n   | 匹配一个换行符                                     |
| \r   | 匹配一个回车符                                     |
| \t   | 匹配一个制表符                                     |
| \v   | 匹配一个垂直制表符                                 |
| \p   | 匹配 CR/LF（等同于 `\r\n`），用来匹配 DOS 行终止符 |



```python
import re

patten = "[a-zA-Z]*(\d+)(\w+)"
str1 = "qwe1234azAA"
res = re.search(patten, str1)
print(res.group(), res.group(0), res.group(1), res.group(2))
# qwe1234azAA qwe1234azAA 1234 azAA
```



**Group用法：**

- 有几个()就有几个group；
- group() = group(0)表示全部匹配结果， group(1)表示第一个匹配块，以此类推；



------



### What the f*ck Python!



- [x] What the f*ck Python：https://github.com/robertparley/wtfpython-cn



------

