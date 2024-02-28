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

```python
# 多进程需要调用Process，进程池Pool会自动管理子进程，Pool只会传入单个参数
import multiprocessing

pool=multiprocessing.Pool(num)   # num代表进程池中的最大进程数
```



```python
# 函数 func2 需要传入多个参数，把它改成一个参数，无论直接让args作为一个元组tuple、词典dict、类class都可以
import time
from multiprocessing import Pool


def func2(args):  # multiple parameters
    x = args[0]
    y = args[1]

    time.sleep(2)  # pretend it is a time-consuming operation
    return x - y


def run__pool():  # main process
    cpu_worker_num = 3
    process_args = [(1, 1), (9, 9), (4, 4), (3, 3), ]

    print(f'-> inputs:  {process_args}')
    start_time = time.time()
    with Pool(cpu_worker_num) as p:
        outputs = p.map(func2, process_args)
    print(f'-> outputs: {outputs}    TimeUsed: {time.time() - start_time:.1f}    \n')


if __name__ == '__main__':
    run__pool()

```



**管道Pipe**

管道的两端可以放在主进程或子进程内，两端可以同时放进去东西，放进去的对象都经过了深拷贝：用 conn.send()在一端放入，用 conn.recv() 另一端取出，管道的两端可以同时给多个进程。

```python
import time
from multiprocessing import Process, Pipe


def func_pipe1(conn, p_id):
    print("func_pipe1 {} start===============\n".format(p_id))
    time.sleep(0.1)
    conn.send(f'{p_id}_send_1')
    print('func_pipe1: {} send_1\n'.format(p_id))

    time.sleep(0.1)
    conn.send(f'{p_id}_send_2')
    print('func_pipe1: {} send_2\n'.format(p_id))

    time.sleep(0.1)
    recv = conn.recv()
    print('func_pipe1: {} recv {}\n'.format(p_id, recv))

    time.sleep(0.1)
    recv = conn.recv()
    print('func_pipe1: {} recv {}\n'.format(p_id, recv))
    print("func_pipe1 {} end=================\n".format(p_id))


def func_pipe2(conn, p_id):
    print("func_pipe2 {} start===============\n".format(p_id))
    time.sleep(0.1)
    conn.send(p_id)
    print('func_pipe2: {} send\n'.format(p_id))
    time.sleep(0.1)
    rec = conn.recv()
    print('func_pipe2: {} recv {}\n'.format(p_id, rec))
    print("func_pipe2 {} end=================\n".format(p_id))


def run__pipe():
    main_conn, child_conn = Pipe()

    process = [Process(target=func_pipe1, args=(main_conn, 'pid_1')),
               Process(target=func_pipe2, args=(child_conn, 'pid_2')),
               Process(target=func_pipe2, args=(child_conn, 'pid_3')), ]

    [p.start() for p in process]
    print('run__pipe send：None\n')
    main_conn.send(None)
    print('run__pipe recv：{}\n'.format(child_conn.recv()))
    [p.join() for p in process]


if __name__ == '__main__':
    run__pipe()
    
'''
run__pipe send：None

run__pipe recv：None

func_pipe2 pid_2 start===============

func_pipe1 pid_1 start===============

func_pipe2 pid_3 start===============

func_pipe2: pid_2 send

func_pipe1: pid_1 send_1

func_pipe2: pid_3 send

func_pipe2: pid_3 recv pid_1_send_1

func_pipe2 pid_3 end=================
func_pipe1: pid_1 send_2


func_pipe2: pid_2 recv pid_1_send_2

func_pipe2 pid_2 end=================

func_pipe1: pid_1 recv pid_2

func_pipe1: pid_1 recv pid_3

func_pipe1 pid_1 end=================
'''
```



