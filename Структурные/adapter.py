'''
Адаптер — это структурный паттерн, который позволяет подружить несовместимые
объекты.

Адаптер выступает прослойкой между двумя объектами, превращая вызовы одного в
вызовы понятные другому.

Применимость: Паттерн можно часто встретить в Python-коде, особенно там, где
требуется конвертация разных типов данных или совместная работа классов с
разными интерфейсами.

Признаки применения паттерна:
Адаптер получает конвертируемый объект в конструкторе или через параметры своих
методов. Методы Адаптера обычно совместимы с интерфейсом одного объекта. Они
делегируют вызовы вложенному объекту, превратив перед этим параметры вызова в
формат, поддерживаемый вложенным объектом.
'''


class Target:
    '''
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    '''
    def request(self) -> str:
        return "Target: The default target's behavior."

class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class AdapterInheritance(Target, Adaptee):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом благодаря множественному наследованию.
    """
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


class AdapterComposition(Target, Adaptee):

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"

def clicode(target: Target) -> None:
    print(target.request(), end="")

if __name__ == '__main__':
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    clicode(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = AdapterInheritance()
    clicode(adapter)
