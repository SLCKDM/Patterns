'''
Одиночка — это порождающий паттерн, который гарантирует существование только
одного объекта определённого класса, а также позволяет достучаться до этого
объекта из любого места программы.

Одиночка имеет такие же преимущества и недостатки, что и глобальные переменные.
Его невероятно удобно использовать, но он нарушает модульность вашего кода.

Вы не сможете просто взять и использовать класс, зависящий от одиночки в другой
программе. Для этого придётся эмулировать присутствие одиночки и там. Чаще
всего эта проблема проявляется при написании юнит-тестов.
'''
import random
from threading import Lock, Thread
from time import perf_counter, sleep
from typing import Any

class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):

    def __init__(self, __value, /):
        self.value = __value

    def some_business_logic(self):
        ...

def test_singleton(__value, /):
    sleep(random.randint(0, 2))
    s = Singleton(__value)
    print(s.value)

def main():
    p3 = Thread(target=test_singleton, args=('3',))
    p2 = Thread(target=test_singleton, args=('2',))
    p1 = Thread(target=test_singleton, args=('1',))
    p4 = Thread(target=test_singleton, args=('4',))
    p4.start()
    p2.start()
    p3.start()
    p1.start()

if __name__ == '__main__':
    while True:
        t0 = perf_counter()
        main()
        print(perf_counter() - t0)
        sleep(1)