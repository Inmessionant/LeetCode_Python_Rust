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
               Process(target=function1, args=(2,))] # Process开启了多进程，不涉及进程通信
    
    [p.start() for p in process]  # 开启了两个进程
    [p.join() for p in process]  # 等待两个进程依次结束


# 正确做法：主线程只能写在if __name__ =='__main__'内部
if __name__ == '__main__':
    run__process()
    

'''
Process开启了多进程，不涉及进程通信，当把一个串行任务编排成多进程时，还需要多进程通信：
  - 进程池Pool 可以让主程序获得子进程的计算结果；（不灵活）
  - 管道Pipe 队列Queue 等可以让进程之间进行通信；（灵活）
  - 共享值Value 共享数组Array 共享内容shared_memory；
'''
```



Python多进程可以选择两种创建进程的方式：

- **fork：**会直接复制一份自己给子进程运行，并把自己所有资源的handle 都让子进程继承；
- **spawn：**只会把必要的资源的handle 交给子进程；

```python
multiprocessing.set_start_method('spawn')  # default on WinOS or MacOS 创建速度快，但更占内存
multiprocessing.set_start_method('fork')   # default on Linux (UnixOS) 创建速度快，但更占内存
```



**进程池Pool**









