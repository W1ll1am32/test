import threading
import time
import queue
import random

cond_var_p = threading.Condition()
cond_var_c = threading.Condition()


def producer(thread_id):
    cond_var_p.acquire()
    while not event.is_set():
        cond_var_p.wait()
        product = random.randint(1, 101)
        stock.put(product)
        cond_var_p.notify()
    cond_var_p.notify_all()
    cond_var_p.release()


def consumer(thread_id):
    cond_var_c.acquire()
    while not event.is_set():
        cond_var_c.wait()
        product = stock.get()
        print("Consumer {} got {} from the stock".format(thread_id + 1, product))
        cond_var_c.notify()
    cond_var_c.notify_all()
    cond_var_c.release()


if __name__ == '__main__':
    threads_p = []
    threads_c = []
    stock = queue.Queue()
    event = threading.Event()

    p = int(input("Input a number of producers: "))
    c = int(input("Input a number of consumers: "))
    for i in range(p):
        t = threading.Thread(target=producer, args=(i,))
        threads_p.append(t)
        t.start()
    for i in range(c):
        t = threading.Thread(target=consumer, args=(i,))
        threads_c.append(t)
        t.start()

    time.sleep(0.1)
    cond_var_p.acquire()
    cond_var_c.acquire()
    cond_var_p.notify()
    cond_var_c.notify()
    cond_var_c.release()
    cond_var_p.release()

    time.sleep(0.1)
    event.set()

    for thread in threads_p:
        thread.join()
    for thread in threads_c:
        thread.join()
