import threading
import time

cond_var = threading.Condition()


def print_num(thread_id, loop_num):
    cond_var.acquire()
    for j in range(loop_num):
        cond_var.wait()
        print(thread_id, end='')
        cond_var.notify()
    cond_var.release()


if __name__ == '__main__':
    threads = []
    n = int(input())
    for i in range(1, 4):
        t = threading.Thread(target=print_num, args=(i, n,))
        threads.append(t)
        t.start()
    time.sleep(0.1)
    cond_var.acquire()
    cond_var.notify()
    cond_var.release()
    for thread in threads:
        thread.join()
