from __future__ import annotations
from abc import ABC, abstractmethod

class Creater(ABC):

    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f'Creator: The same Creator`s code has just worked with {product.operation}'
        return result


class Creater1(Creater):

    def factory_method(self):
        return Product1()


class Creater2(Creater):

    def factory_method(self):
        return Product2()


class Product(ABC):

    @abstractmethod
    def operation(self):
        pass


class Product1(Product):
    def operation(self):
        return '{Result of Product1}'


class Product2(Product):
    def operation(self):
        return '{Result of Product2}'


if __name__ == '__main__':
    Creater1