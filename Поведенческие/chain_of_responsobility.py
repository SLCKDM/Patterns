'''
Цепочка обязанностей - поведенческий паттерн, позволяющий передавать запрос по
цепочке потенциальных обработчиков, пока один из них не обработает запрос.

Избавляет от жёсткой привязки отправителя запроса к его получателю, позволяя
выстраивать цепь из различных обработчиков динамически.

Применимость: Паттерн встречается в Python не так уж часто, так как для его
применения нужна цепь объектов, например, связанный список.

Признаки применения паттерна: Цепочку обязанностей можно определить по спискам
обработчиков или проверок, через котрые пропускаются запросы. Особенно если
порядок следования обработчиков важен.
'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class AbstractHandler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler: ...

    @abstractmethod
    def handle(self, request) -> str | None: ...

class Handler(AbstractHandler):
    """
    Поведение цепочки по умолчанию может быть реализовано внутри базового
    класса обработчика.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

"""
Все конкретные Обработчики либо обрабатывают запрос, либо передают его
следующему обработчику в цепочке.
"""


class MonkeyHandler(Handler):

    def handle(self, request: Any) -> str:
        if request == 'Banana':
            return f'Monkey: i`ll eat the {request}'
        else:
            return super().handle(request)


class SquirrelHandler(Handler):

    def handle(self, request: Any) -> str:
        if request == 'Nut':
            return f'Squirell: i`ll eat the {request}'
        else:
            return super().handle(request)


class DogHandler(Handler):

    def handle(self, request: Any) -> str:
        if request == 'MeatBall':
            return f'Dog: i`ll eat the {request}'
        else:
            return super().handle(request)


def client_code(handler: Handler):
    for food in ['Banana', 'Nut', 'Cup of coffee']:
        print(f'Client: Who wants a {food}?')
        result = handler.handle(food)
        if result:
            print(f'    {result}')
        else:
            print(f'    {food} was left untouched')

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(
    squirrel).set_next(
    dog)

    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")
    print("Subchain: Squirrel > Dog")
    client_code(squirrel)