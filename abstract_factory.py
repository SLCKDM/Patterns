'''
Абстрактная фабрика - это пораждающий паттерн проектирования, который решает
проблему создания семейств связанных продуктов, без указания конкеретных
классов продуктов

Абстрактная фабрика задает интерфейс создания всех доступных типов продуктов, а
каждая конкретная реализация фабрики порождает продукты одной из вариаций.
Клиентский код вызывает методы фабрики для получения продуктов, вместо
самостоятельного создания с помощью оператора `new`. При этом фабрика сама
следит за тем, чтобы создать продукт нужной вариации.

Применяемость: паттерн можно часто встретить в Python-коде, особенно там, где
требуется создание семейств продуктов (например, внутри фреймворка)

Признаки применения паттерна: паттерн можно определить по методам, возвращающим
фабрику, которая, в свою очередь, используется для создания конкретных
продуктов, возвращая их через абстрактные типы или интерфейсы.
'''

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    '''
    Интерфейс Абстрактной фабрики объявялет набор методов, которые возвращают
    различные абстрактные продукты. Эти продукты называются семейством и
    связаны темой или концепцией высокого уровня. Продукты одного семейства
    обычно могут взаимодействовать между собой. Семейство продуктов может иметь
    несколько вариаций, но продукты одной вариации несовместимы с продуктами
    другой.
    '''

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    '''
    Конкретная Фабрика производит семейство продуктов одной вариации. Фабрика
    гарантирует совместимость полученных продуктов. Обратите внимание, что
    сигнатуры методов Конкретной Фаборики возвращают абстрактный продукт, в то
    время как внутри методам создается экземпляр конкретного продукта.
    '''

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    '''
    Каждая конкретная фабрика имеет соответствующую вариацию продукта.
    '''

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_a(self) -> str: pass


class AbstractProductB(ABC):
    '''
    Базовый интерфейс другого продукта. Все продукты могут
    взаимодействовать друг с другом, но правильное взаимодействие возможно
    только между продуктами одной и той же конкретной вариации.
    '''

    @abstractmethod
    def useful_function_b(self) -> str:
        '''
        Продукт B способен работать самостоятельно...
        '''
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        '''
        а также взаимодействовать с Продуктами А в той же вариации.

        Абстрактная фабрика гарантирует, что все продукты, которые она создает,
        имеют одинаковую вариацию и, следовательно, совестимы.
        '''
        pass


class ConcreteProductA1(AbstractProductA):

    def useful_function_a(self):
        return 'The result of the product A1.'


class ConcreteProductA2(AbstractProductA):

    def useful_function_a(self):
        return 'The result of the product A2.'


class ConcreteProductB1(AbstractProductB):

    def useful_function_b(self):
        return 'The result of the product B1.'

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f'The result of the B1 collaborating with the {result}'


class ConcreteProductB2(AbstractProductB):

    def useful_function_b(self):
        return 'The result of the product B2.'

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f'The result of the B2 collaborating with the {result}'


def clicode(factory: AbstractFactory) -> None:
    prod_a = factory.create_product_a()
    prod_b = factory.create_product_b()

    print(f'{prod_b.useful_function_b()}')
    print(f'{prod_b.another_useful_function_b(prod_a)}')

if __name__ == '__main__':
    print('Client: Testing client code with the first factory type:')
    clicode(ConcreteFactory1())
    print('\n')
    print('Client: Testing the same client code with the second factory type:')
    clicode(ConcreteFactory2())