------

#### 参考引用



- [x] **Algorithm-Pattern: https://github.com/greyireland/algorithm-pattern**
- [x] **代码随想录: https://programmercarl.com/**



------



#### 多进程



- **多进程：**多个CPU核心一起同时做多件事，不至于一个CPU核心干活而其他CPU核心空闲；
- **多线程：**单个CPU核心可以在多个线程之间来回切换，同时做几件事，不至于卡在某一步；



```
为何在Python里用多进程这么麻烦？Python的线程是操作系统线程，因此要有Python全局解释器锁。一个python解释器进程内有一条主线程，以及多条用户程序的执行线程。即使在多核CPU平台上，由于GIL的存在，所以禁止多线程的并行执行。

1. Python 3.2，Python无法靠自己实现多进程；
2. Python 3.5，要么用Python调用C语言，要么需要在外部执行；
3. Python 3.6，multiprocessing库，可以进行进程间的通信，以及有限的内存共享；
4. Python 3.8，shared_memory；
```



**子进程Process**

```python
from multiprocessing import Process


def function1(id):  # 子进程
    print(f'id:  {id}')


def run__process():  # 主进程
    process = [Process(target=function1, args=(1,)),
               Process(target=function1, args=(2,))]
    [p.start() for p in process]  # 开启了两个进程
    [p.join() for p in process]  # 等待两个进程依次结束


# 正确做法：主线程只能写在if __name__ =='__main__'内部
if __name__ == '__main__':
    run__process()
```

