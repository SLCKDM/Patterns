'''
Декоратор - это структурный паттерн, который позволяет добавлять объектам новые
поведения на лету, помещая их в новые объекты-обёртки.

Декоратор позволяет оборачивать объекты бесчисленное количествао раз благодаря
тому, что и обёртки, и реальные оборачиваемые объекты имеют общий интерфейс.

Применяемость: Паттерн млэно встретить в Python-коде, особенно в коде,
работающем с потоками данных.

Признаки применения паттерна: декоратор можно распознать по создающим методам,
которые принимают в парамтерах объекты того же абстрактного типа или интерфейса,
что и текущий класс.
'''
from abc import ABC, abstractmethod


class Component(ABC):
    '''
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    '''

    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    ''' Конкретные Компоненты предоставляют реализации поведения по умолчанию.
    Может быть несколько вариаций этих классов. '''

    def operation(self) -> str:
        return self.__class__.__name__


class Decorator(Component):
    '''
    Базовый класс Декоратора следует тому же интерфейсу, что и другие компоненты.
    Оснонвая цель этого класса - определить интерфейс обёртки для всех
    конкретных декораторов. Реализация кода обёртки по умолчанию может включать
    в себя поле для хранения завёрнутого компонента и средства его инициализации.
    '''

    _component: Component

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        '''
        Декоратор делегирует всю работу обёрнутому компоненту.
        '''
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    '''
    Конкретные Декораторы вызывают обёрнутый объект и изменяют его результат
    некоторым образом.
    '''

    def operation(self) -> str:
        '''
        Декораторы могут вызывать родительскую реализацию операции, вместо
        того, чтобы вызывать обёрнутый объект напрямую. Такой подход упрощает
        расширение классов декораторов.
        '''
        print('*ConcreteDecoratorA: DOES SOMETHING BEFORE WRAPPED OBJECT CALL*')
        return f'ConcreteDecoratorA({self._component.operation()})'


class ConcreteDecoratorB(Decorator):
    '''
    Декораторы могут выполнять поведение до или после вызова обёрнутого объекта.
    '''

    def operation(self) -> str:
        res = f'ConcreteDecoratorB({self._component.operation()})'
        print('*ConcreteDecoratorB: DOES SOMETHING after WRAPPED OBJECT CALL*')
        return res

def client_code(component: Component):
    '''
    Клментский код работает со всеми объектамиЮ используя интерфейс Компонента.
    Таким образом, он остаётся независимым от конкретных классов компонентов, с
    которыми работает.
    '''
    print(f'RESULT: {component.operation()}', end='')


if __name__ == '__main__':
    simple = ConcreteComponent()
    print('Client: I`ve got a simple component:')
    client_code(simple)
    print('\n')

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print('Client: Now I`ve got a decorated component:')
    client_code(decorator2)