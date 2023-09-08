'''
Компоновщик - это структурный паттерн, который позволяет создавать дерево
объектов и работать с ним так же, как и с едининчным объектом.

Компоновщик давно стал синонимом всех задач, связанных с построеникм дерева
объектов. Все операции компоновщика основаны на рекурсии и "суммировании"
результатов на ветвях дерева.

Применимость: Паттерн Компоновщик встречается в любых задачах, которые связаные
с построением дерева. Самый простой пример - составные элементы GUI, которые
тоже можно рассматривать как дерево

Признаки применения паттерна: Если из объектов строится древовидная структура,
и со всеми объектами дерева, как и с самим деревом работают через общий
интерфейс.
'''

from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):
    ''' Базовый класс Компонент объявляет общие операции как для простых, так и
    для сложных объектов структуры.
    '''

    @property
    def parent(self) -> Component|None:
        return self._parent

    @parent.setter
    def parent(self, parent: Component|None):
        self._parent = parent

    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    ''' Класс Лист представляет собой конечные объекты структуры. Лист не может
    иметь вложенных компонентов.

    Обычно объекты Листьев выполняют фактическую работу, тогда как объекты
    Контейнера лишь делегируют работу своим подкомпонентам.
    '''

    def operation(self):
        return 'Leaf'

class Composite(Component):
    ''' Класс Контейнер содержит сложные компоненты, которые могут иметь вложенные
    компоненты. Обычно обхекты Контейнеры делегируют фактическую работу своим
    детям, а затем "Суммируют" результат.
    '''

    def __init__(self) -> None:
        self._children: list[Component] = []

    def add(self, component: Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f'Branch({"+".join(results)})'

def client_code(component: Component):
    print(f'Result: {component.operation()}', end='')

def client_code2(component1: Component, component2: Component):
    if component1.is_composite():
        component1.add(component2)
    print(f"RESULT: {component1.operation()}", end="")
if __name__ == "__main__":
    simple = Leaf()
    print('Client: I`ve got a simple component:')
    client_code(simple)
    print('\n')

    tree = Composite()
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print('Client: now i`ve got a composite tree:')
    client_code(tree)
    print('\n')

    print('Client: I don`t need to check the components classes even when managing the tree:')
    client_code2(tree, simple)