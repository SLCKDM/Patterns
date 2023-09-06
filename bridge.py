'''
Мост — это структурный паттерн, который разделяет бизнес-логику или большой
класс на несколько отдельных иерархий, которые потом можно развивать отдельно
друг от друга.

Одна из этих иерархий (абстракция) получит ссылку на объекты другой иерархии
(реализация) и будет делегировать им основную работу. Благодаря тому, что все
реализации будут следовать общему интерфейсу, их можно будет взаимозаменять
внутри абстракции.

Применимость: Паттерн Мост особенно полезен когда вам приходится делать
кросс-платформенные приложения, поддерживать несколько типов баз данных или
работать с разными поставщиками похожего API (например, cloud-сервисы,
социальные сети и т. д.)

Признаки применения паттерна: Если в программе чётко выделены классы
«управления» и несколько видов классов «платформ», причём управляющие объекты
делегируют выполнение платформам, то можно сказать, что у вас используется Мост.
'''

from __future__ import annotations
from abc import ABC, abstractmethod
from sys import implementation


class Abstraction:
    """
    Абстракция устанавливает интерфейс для «управляющей» части двух иерархий
    классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
    ему всю настоящую работу.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self):
        return (f'Abstraction: Base operation with:\n'
                f'{self.implementation.operation()}')

class ExtendedAbstraction(Abstraction):
    """
    Можно расширить Абстракцию без изменения классов Реализации.
    """
    def operation(self):
        return (f'ExtendedAbstraction: Base operation with:\n'
                f'{self.implementation.operation()}')

class Implementation(ABC):
    """
    Реализация устанавливает интерфейс для всех классов реализации. Он не должен
    соответствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
    совершенно разными. Как правило, интерфейс Реализации предоставляет только
    примитивные операции, в то время как Абстракция определяет операции более
    высокого уровня, основанные на этих примитивах.
    """

    @abstractmethod
    def operation(self):
        ...

"""
Каждая Конкретная Реализация соответствует определённой платформе и реализует
интерфейс Реализации с использованием API этой платформы.
"""

class ConcreteImplementationA(Implementation):

    def operation(self):
        return 'ConcreteImplementationA: here`s the result on the platfrom A'

class ConcreteImplementationB(Implementation):

    def operation(self):
        return 'ConcreteImplementationB: here`s the result on the platfrom B'

def client_code(abstraction: Abstraction):
    print(abstraction.operation(), end="")

if __name__ == '__main__':
    implementation = ConcreteImplementationA()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

    print('\n')

    implementation = ConcreteImplementationB()
    abstraction = Abstraction(implementation)
    client_code(abstraction)