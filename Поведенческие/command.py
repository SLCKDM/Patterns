"""
Команда - это поведенческий паттерн, позволяющий заворачивать запросы или
простые операции в отдельные объекты.

Это позволяет откладывать выполнение команд, выстраивать их в очереди, а также
хранить историю и делать отмену.

Применимость: паттерн можно встретить когда нужно откладывать выполнение команд,
выстраивать их в очереди, а также хранить историю и делать отмену.

Признаки применения паттерна: классы команд построены вокруг одного действия и
имеют очень узкий контекст. Объекты команд часто подаются в обработчики событий
элементов GUI. Практически любая реализация отмены использует принцип команд.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    Интерфейс Команды объявляет метод для выполнения команд.
    """

    @abstractmethod
    def execute(self) -> None: ...


class SimpleCommand(Command):
    """
    Некоторые команды способны выполнять простые операции самостоятельно.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print("SimpleCommand: See, i can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    """
    Но есть и команды, которые делегируют более сложные операции другим
    объектам, называемыми "Получателеми".
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Сложные команды могут принимать один или несколько объектов-получателей
        вместе с любыми данными о контексте через конструктор.
        """
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Команды могут делегировать выполнение любым методам получателя.
        """
        print("ComplexCommand: Complex stuff should be done by a receiver object")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:
    """
    Классы Получаталей содержат некую важную бизнес-логику. Они умеют выполнять
    все виды операций, связанных с выпонением запроса. Фактически, любой класс
    может выступать Получателем.
    """

    def do_something(self, a: str) -> None:
        print(f'Receiver: Working on ({a}.)')

    def do_something_else(self, b: str) -> None:
        print(f'Receiver: Also working on ({b}.)')


class Invoker:
    """
    Отправитель связан с одной или несколькими командами. Он отправляет запрос
    команде.
    """

    _on_start = None
    _on_finish = None

    # Инициализация команд

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self):
        """
        Отправитель не зависит от классов конкретных команд и получателей.
        Отправитель передаёт запрос получателю косвенно, выполняя команду.
        """
        print("Invoker: Does anynody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ... doing something really important...")

        print("Invoker: Does anybody want something done before i finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == '__main__':
    """
    Клиентский код может параметризировать отправителя любыми командами.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand('Say Hi'))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, 'Send email', 'Save report'))

    invoker.do_something_important()
    print()

