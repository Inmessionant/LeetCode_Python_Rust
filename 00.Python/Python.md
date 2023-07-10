------



## 01. Regex



- Guide：https://github.com/ziishaned/learn-regex/blob/master/translations/README-cn.md
- 练习网站：https://regex101.com/



```
- 正则表达式是大小写敏感，所以The不会匹配the；
```



#### 01. 元字符

| 元字符 | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| .      | `.`匹配任意单个字符，但不匹配换行符                          |
|        | ".ar" => The **car par**ked in the **gar**age.               |
|        |                                                              |
| [ ]    | 方括号用来指定一个字符集，在方括号中使用连字符来指定字符集的范围，在方括号中的字符集不关心顺序 |
|        | "[Tt]he" => **The** car parked in **the** garage.            |
|        | 方括号的句号就表示句号，"ar[.]" => A garage is a good place to park a c**ar.** |
|        |                                                              |
| [^ ]   | 一般来说 `^` 表示一个字符串的开头，但它用在一个方括号的开头的时候，它表示这个字符集是否定的 |
|        | "[^c]ar" => The car **par**ked in the **gar**age.            |
|        |                                                              |
| *      | 在`*`之前的字符出现 >=0                                      |
|        | "[a-z]*" => **The car parked in the garage** #21.            |
|        | `*`字符和`.`字符搭配可以匹配所有的字符`.*`                   |
|        | `*`和表示匹配空格的符号`\s`连起来用，如表达式`\s*cat\s*`匹配0或更多个空格开头和0或更多个空格结尾的cat字符串 |
|        |                                                              |
| +      | `+`号之前的字符出现>=1                                       |
|        | "c.+t" => The fat **cat sat on the mat**.                    |
|        |                                                              |
| ?      | 元字符 `?` 标记在符号前面的字符为可选，即出现 0 或 1 次      |
|        | 表达式 `[T]?he` 匹配字符串 `he` 和 `The`，"[T]he" => **The** car is parked in the garage. |
|        |                                                              |
| {n,m}  | 在正则表达式中 `{}` 是一个量词，常用来限定一个或一组字符可以重复出现的次数 (n <= num <= m) |
|        | 表达式 `[0-9]{2,3}` 匹配最少 2 位最多 3 位 0~9 的数字："[0-9]{2,3}" => The number was 9.**999**7 but we rounded it off to **10**.0. |
|        | 可以省略第二个参数，`[0-9]{2,}` 匹配至少两位 0~9 的数字："[0-9]{2,}" => The number was 9.**9997** but we rounded it off to **10**.0. |
|        | 如果逗号也省略掉则表示重复固定的次数，`[0-9]{3}` 匹配3位数字："[0-9]{3}" => The number was 9.**999**7 but we rounded it off to 10.0. |
|        |                                                              |
| (...)  | `(...)` 中包含的内容将会被看成一个整体，和数学中小括号（ ）的作用相同 |
|        | (ab)*` 匹配连续出现 0 或更多个 `ab，如果没有使用 `(...)` ，那么表达式 `ab*` 将匹配连续出现 0 或更多个 `b`，`(...){n}` 则表示整个标群内的字符重复n次 |
|        | ()` 中用或字符 `|` 表示或`，`(c|g|p)ar` 匹配 `car` 或 `gar` 或 `par` |
|        |                                                              |
| \|     | 或运算符，匹配符号前或后的字符                               |
|        | "(T\|t)he\|car" => **The** **car** is parked in **the** garage. |
|        |                                                              |
| \      | 反斜线 `\` 在表达式中用于转码紧跟其后的字符。用于指定 `{ } [ ] / \ + * . $ ^ |?` 这些特殊字符，如果想要匹配这些特殊字符则要在其前面加上反斜线 `\` |
|        | "(f\|c\|m)at\.?" => The **fat cat** sat on the **mat.**      |
|        |                                                              |
| ^      | `^` 用来检查匹配的字符串是否在所匹配字符串的开头，例如，在 `abc` 中使用表达式 `^a` 会得到结果 `a`。但如果使用 `^b` 将匹配不到任何结果。因为在字符串 `abc` 中并不是以 `b` 开头 |
|        | "^(T\|t)he" => **The** car is parked in the garage.    `^(T|t)he` 匹配以 `The` 或 `the` 开头的字符串 |
|        |                                                              |
| $      | `$` 号用来匹配字符是否是最后一个                             |
|        | "(at\.)" => The fat c**at.** sat. on the m**at.** ，`(at\.)$` 匹配以 `at.` 结尾的字符串，"(at\.)" => The fat cat. sat. on the **mat.** |



#### 02. 字符集

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



#### 03. 标志

标志也叫模式修正符，因为它可以用来修改表达式的搜索结果。 这些标志可以任意的组合使用，它也是整个正则表达式的一部分

| 标志 | 描述                                                         |
| ---- | ------------------------------------------------------------ |
| i    | 忽略大小写                                                   |
|      | 表达式 `/The/gi` 表示在全局搜索 `The`，在后面的 `i` 将其条件修改为忽略大小写，则变成搜索 `the` 和 `The`，`g` 表示全局搜索，"The" => **The** fat cat sat on the mat.      "/The/gi" => **The** fat cat sat on **the** mat. |
|      |                                                              |
| g    | 修饰符 `g` 常用于执行一个全局搜索匹配，即（不仅仅返回第一个匹配的，而是返回全部） |
|      | 表达式 `/.(at)/g` 表示搜索 任意字符（除了换行）+ `at`，并返回全部结果，"/.(at)/" => The **fat** cat sat on the mat.         "/.(at)/g" => The **fat cat sat** on the **mat**. |
|      |                                                              |
| m    | 多行修饰符 `m` 常用于执行一个多行匹配，像之前介绍的 `(^,$)` 用于检查格式是否是在待检测字符串的开头或结尾。但我们如果想要它在每行的开头和结尾生效，我们需要用到多行修饰符 `m`。例如，表达式 `/at(.)?$/gm` 表示小写字符 `a` 后跟小写字符 `t` ，末尾可选除换行符外任意字符。根据 `m` 修饰符，现在表达式匹配每行的结尾。 |
|      | "/.at(.)?$/" => The fat\n            cat sat\n                  on the **mat.** |
|      | "/.at(.)?$/gm" => The **fat**\n                   cat **sat**\n                   on the **mat.** |
|      |                                                              |



#### 04. 贪婪匹配与惰性匹配

正则表达式默认采用贪婪匹配模式，在该模式下意味着会匹配尽可能长的子串。我们可以使用 `?` 将贪婪匹配模式转化为惰性匹配模式。

|                                                |
| ---------------------------------------------- |
| "/(.*at)/" => **The fat cat sat on the mat**.  |
| "/(.*?at)/" => **The fat** cat sat on the mat. |



- “?”元字符规定其前导对象必须在目标对象中连续出现**零次或一次**，如：abc(d)?可匹配abc和abcd；
- 当该字符紧跟在任何一个其他限制符`·*,+,?，{n}，{n,}，{n,m}`后面时，**匹配模式是非贪婪的**，非贪婪模式尽可能少的匹配所搜索的字符串，例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配“oooo”；源字符串`str=“dxxddxxd”`中，`d\w*?`会匹配 dx,而`d\w*?d`会匹配 dxxd；



#### 05. re包匹配（常用）

```python
import re

patten = "[a-zA-Z]*(\d+)(\w+)"
str1 = "qwe1234azAA"
res = re.search(patten, str1)
print(res.group(), res.group(0), res.group(1), res.group(2))
# res.group(): qwe1234azAA 
# res.group(0): qwe1234azAA 
# res.group(1): 1234 
# res.group(2): azAA


Group用法：
	1.有几个()就有几个group；
	2.group() = group(0)表示全部匹配结果， group(1)表示第一个匹配块，以此类推；
```





------



## 02. What the f*ck Python!



- [x] What the f*ck Python：https://github.com/robertparley/wtfpython-cn



------





## 03. Python 



#### 01. match

```python
1.
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case _:  #  通配符 并必定会匹配成功
            return "Something's wrong with the internet"

     
2. 使用 | （“ or ”）在一个模式中可以组合多个字面值
case 401 | 403 | 404:
    return "Not allowed"
          
            
3.为模式添加成为守护项的 if 子句。如果守护项的值为假，则 match 继续匹配下一个 case 语句块     
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")          
```



#### 02. keyword argument

```python
1.函数调用时，关键字参数必须跟在位置参数后面；


2. *arguments形参接收一个元组  **keywords形参接收一个字典
def cheeseshop(kind, *arguments, **keywords): 
    pass


3.
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only

3.1 函数定义中未使用 / 和 * 时，参数可以按位置或关键字传递给函数;
3.2 特定形参可以标记为仅限位置。仅限位置时，形参的顺序很重要，且这些形参不能用关键字传递。仅限位置形参应放在 / （正斜杠）前。/ 用于在逻辑上分割仅限位置形参与其它形参。如果函数定义中没有 /，则表示没有仅限位置形参。 / 后可以是 位置或关键字 或 仅限关键字 形参;
3.3 把形参标记为 仅限关键字，表明必须以关键字参数形式传递该形参，应在参数列表中第一个 仅限关键字 形参前添加 *；
```



#### 03. 解包实参

```python
1. 函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。例如，内置的 range() 函数要求独立的 start 和 stop 实参。如果这些参数不是独立的，则要在调用函数时，用 * 操作符把实参从列表或元组解包出来：
list(range(3, 6))            # normal call with separate arguments，[3, 4, 5]
args = [3, 6]
list(range(*args))           # call with arguments unpacked from a list，[3, 4, 5]


2. 字典可以用 ** 操作符传递关键字参数：
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)  # -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```



#### 04. 文档字符串

```python
1. 第一行应为对象用途的简短摘要。不要在这里显式说明对象名或类型，这一行应以大写字母开头，以句点结尾；
2. 文档字符串为多行时，第二行应为空白行，在视觉上将摘要与其余描述分开，后面的行可包含若干段落，描述对象的调用约定、副作用等；
3. Python 解析器不会删除 Python 中多行字符串字面值的缩进，因此，文档处理工具应在必要时删除缩进。这项操作遵循以下约定：文档字符串第一行之后的第一个非空行决定了整个文档字符串的缩进量，然后删除字符串中所有行开头处与此缩进“等价”的空白符，不能有比此缩进更少的行，但如果出现了缩进更少的行，应删除这些行的所有前导空白符；

def my_function():
    """Do nothing, but document it.   

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```



#### 05. 数据结构



**list & collections.deque**

```python
list.append(x)
在列表末尾添加一个元素，相当于 a[len(a):] = [x] 。

list.extend(iterable)
用可迭代对象的元素扩展列表。相当于 a[len(a):] = iterable 。

list.insert(i, x)
在指定位置插入元素。第一个参数是插入元素的索引，因此，a.insert(0, x) 在列表开头插入元素， a.insert(len(a), x) 等同于 a.append(x) 。

list.remove(x)
从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 ValueError 异常。

list.pop([i])
删除列表中指定位置的元素，并返回被删除的元素。未指定位置时，a.pop() 删除并返回列表的最后一个元素。（方法签名中 i 两边的方括号表示该参数是可选的，不是要求输入方括号。这种表示法常见于 Python 参考库）。

list.clear()
删除列表里的所有元素，相当于 del a[:] 。

list.index(x[, start[, end]])
返回列表中第一个值为 x 的元素的零基索引。未找到指定元素时，触发 ValueError 异常。

可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。

list.count(x)
返回列表中元素 x 出现的次数。

list.sort(*, key=None, reverse=False)
就地排序列表中的元素（要了解自定义排序参数，详见 sorted()）。

list.reverse()
翻转列表中的元素。

list.copy()
返回列表的浅拷贝。相当于 a[:] 。
```


