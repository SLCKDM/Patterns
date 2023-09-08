'''
Легковес - структурный паттерн, который экономит память, благодаря разделению
общего состояния, вынесенного в один объект, между множеством объектов.

Легковес позволяет экономить память, кешируя одинаковые данные, используемые в
разных объектах.

Применение: Весь смысл использования Легковеса - в экономии памяти. Поэтому,
если в приложении нет такой проблемы, то вы врядли найдете там примеры
Легковеса.


Признаки применения паттерна: Легковес можно определить по создающти методам
класса, которые возвращают закешированные объекты, вместо создания новых.
'''

import json


class Flyweight:
    '''
    Легковес хранит общую часть состояния (также называемую внутренним
    состоянием), которая принадлежит нескольим реальным бизнес-объектам.
    Легковес принимает оставшуюся часть состояния (внешнее состояние,
    уникальное для каждого объекта) через его параметры метода.
    '''

    def __init__(self, shared_state: dict) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory:
    '''
    Фабрика легковесов создает объекты-Легковесы и управляет ими. Она
    обеспечивает правильноек разделение легковесов. Когда клиент запрашивает
    легковес, фабрика либо возвращает существующий экземпляр, либо создает
    новый, если он ещё не существует.
    '''

    _flyweights: dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        '''
        возвращает хэш строки Легковеса с заданным состоянием или создает новый.
        '''
        return '_'.join(sorted(state))

    def get_flyweight(self, shared_state: dict) -> Flyweight:
        '''
        Возвращает существующий легковес
        '''
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            self._flyweights[key] = Flyweight(shared_state)
        return self._flyweights[key]

    def list_flyweights(self):
        print(len(self._flyweights))

def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # Клиентский код либо сохраняет, либо вычисляет внешнее состояние и передает
    # его методам легковеса.
    flyweight.operation([plates, owner])

if __name__ == "__main__":
    """
    Клиентский код обычно создает кучу предварительно заполненных легковесов на
    этапе инициализации приложения.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweights()