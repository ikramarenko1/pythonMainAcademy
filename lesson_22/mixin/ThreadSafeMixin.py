# Многопотокова безпека:
# Створіть мікс, який реалізує механізми многопотокової безпеки,
# такі як блокування або семафори, для об'єктів, які мають бути використані в багатьох потоках.
import threading
import time


class ThreadSafeMixin:
    def __init__(self):
        self._lock = threading.Lock()

    @staticmethod
    def thread_safe_method(func):
        def wrapper(self, *args, **kwargs):
            with self._lock:
                return func(self, *args, **kwargs)

        return wrapper


class Counter(ThreadSafeMixin):
    def __init__(self):
        super().__init__()
        self._count = 0

    @ThreadSafeMixin.thread_safe_method
    def increment(self):
        self._count += 1

    def get_count(self):
        return self._count


def worker(counter):
    for _ in range(1000):
        counter.increment()
        time.sleep(0.001)


counter = Counter()
threads = []

for _ in range(10):
    thread = threading.Thread(target=worker, args=(counter,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Final count:", counter.get_count())

# без использования класса ThreadSafeMixin счетчик мог бы быть поврежден,
# если бы два потока одновременно пытались его увеличить
