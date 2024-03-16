



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

```python
class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
进程对象表示在单独进程中运行的活动，应始终使用关键字参数调用构造函数
- group 应该始终是 None；
- target是由run()方法调用的可调用对象。它默认为 None ，意味着什么都没有被调用；
- name 是进程名称；
- args 是目标调用的参数元组；


start()
启动进程活动，这个方法每个进程对象最多只能调用一次。它会将对象的 run() 方法安排在一个单独的进程中调用

join([timeout])
当我们需要等待所有子进程完成后再继续主进程时，可以使用join()函数来实现；
如果可选参数 timeout 是 None （默认值），则该方法将阻塞，直到调用 join() 方法的进程终止。如果 timeout 是一个正数，它最多会阻塞 timeout 秒
```





**子进程Process**

```python
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
```



```python
from multiprocessing import Process


def function1(id):  # 子进程
    print(f'id:  {id}')


def run__process():  # 主进程
    process = [Process(target=function1, args=(1,)),
               Process(target=function1, args=(2,))] # Process开启了多进程，不涉及进程通信
    
    [p.start() for p in process]  # 启动了两个进程
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



**上下文和启动方法：**

- **fork：**父进程产生 Python 解释器分叉。子进程在开始时实际上与父进程相同，父进程的所有资源都由子进程继承； **- 创建速度快，但更占内存**
- **spawn：**父进程会启动一个新的 Python 解释器进程，子进程将只继承那些运行进程对象的 [`run()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.Process.run) 方法所必须的资源。 特别地，来自父进程的非必需文件描述符和句柄将不会被继承； **- 创建速度快，但更占内存**
- 要选择一个启动方法，你应该在主模块的 `if __name__ == '__main__'` 子句中调用 [`set_start_method()`](https://docs.python.org/zh-cn/3/library/multiprocessing.html#multiprocessing.set_start_method)；



**进程池Pool**

```python
# 多进程需要调用Process，进程池Pool会自动管理子进程
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
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



**进程间交换对象：管道Pipe**

​    管道的两端可以放在主进程或子进程内，两端可以同时放进去东西，放进去的对象都经过了深拷贝：用 conn.send()在一端放入，用 conn.recv() 另一端取出，管道的两端可以同时给多个进程（如果追求运行速度，推荐使用Pipe而不是Queue）

​    如果两个进程（或线程）同时尝试读取或写入管道的同一端，管道中的数据可能会损坏。在不同进程中同时使用管道的不同端的情况下不存在损坏的风险。

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

    process = [Process(target=func_pipe1, args=(main_conn,  'pid_1')),
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

```python
from multiprocessing import Pipe

main_conn, child_conn = Pipe(duplex=True)  # 开启双向管道，管道两端都能存取数据。默认开启

main_conn.send('A')
print(main_conn.poll())  # 会print出 False，因为没有东西等待main_conn去接收
print(child_conn.poll())  # 会print出 True ，因为main_conn send 了个 'A' 等着child_conn 去接收
print(child_conn.recv(), child_conn.poll(2))  # 会等待2秒钟再开始查询，然后print出 'A False'
```



**进程间交换对象：队列Queue**

```python
# 无论主进程或子进程，都能访问到队列，放进去的对象都经过了深拷贝，队列Queue 有基本的队列属性，更加灵活，且队列是线程和进程安全的
import time
from multiprocessing import Process, Queue


def func1(i):
    time.sleep(1)
    print(f'args {i}\n')


def run__queue():
    queue = Queue(maxsize=4)  # the following attribute can call in anywhere
    queue.put(True)
    queue.put([0, None, object])  # you can put deepcopy thing
    print("the length of Queue is: ", queue.qsize())
    print(queue.get())  # First In First Out
    print(queue.get())  # First In First Out
    print("the length of Queue is: ", queue.qsize())

    process = [Process(target=func1, args=(queue,)),
               Process(target=func1, args=(queue,)), ]
    [p.start() for p in process]
    [p.join() for p in process]


if __name__ == '__main__':
    run__queue()
```



**进程间同步**

```python
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()  # 不使用锁的情况下，来自于多进程的输出很容易产生混淆

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
```



**共享内存Manager**

为了在Python里面实现多进程通信，上面提及的 Pipe Queue 把需要通信的信息从内存里深拷贝了一份给其他线程使用（需要分发的线程越多，其占用的内存越多）。而共享内存会由解释器负责维护一块共享内存（而不用深拷贝），这块内存每个进程都能读取到，读写的时候遵守管理（因此不要以为用了共享内存就一定变快）。

Manager可以创建一块共享的内存区域，但是存入其中的数据需要按照特定的格式，Value可以保存数值，Array可以保存数组

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

```python
from multiprocessing import Process, Lock
# 为了更灵活地使用共享内存，可以使用 multiprocessing.sharedctypes 模块，该模块支持创建从共享内存分配的任意ctypes对象
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def modify(n, x, s, A):
    n.value **= 2
    x.value **= 2
    s.value = s.value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2


if __name__ == '__main__':
    lock = Lock()

    n = Value('i', 7)
    x = Value(c_double, 1.0 / 3.0, lock=False)
    s = Array('c', b'hello world', lock=lock)
    A = Array(Point, [(1.875, -6.25), (-5.75, 2.0), (2.375, 9.5)], lock=lock)

    p = Process(target=modify, args=(n, x, s, A))
    p.start()
    p.join()

    print(n.value)
    print(x.value)
    print(s.value)
    print([(a.x, a.y) for a in A])
```

