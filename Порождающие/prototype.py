'''
Прототип — это порождающий паттерн, который позволяет копировать объекты любой
сложности без привязки к их конкретным классам.

Все классы — Прототипы имеют общий интерфейс. Поэтому вы можете копировать
объекты, не обращая внимания на их конкретные типы и всегда быть уверены, что
получите точную копию. Клонирование совершается самим объектом-прототипом, что
позволяет ему скопировать значения всех полей, даже приватных.
'''
import copy


class SelfReferencingEntity:

    def __init__(self) -> None:
        self.parent = None

    def set_parent(self):
        self.parent = self


class SomeComponent:

    def __init__(self, some_int, some_list_of_obj, some_circular_ref) -> None:
        self.some_int = some_int
        self.some_list_of_obj = some_list_of_obj
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        some_list_of_obj = copy.copy(self.some_list_of_obj)
        some_circular_ref = copy.copy(self.some_circular_ref)
        new = self.__class__(
            self.some_int, some_list_of_obj, some_circular_ref
        )
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo: dict | None = None):
        if not memo:
            memo = {}
        some_list_of_obj = copy.deepcopy(self.some_list_of_obj, memo=memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo=memo)
        new = self.__class__(
            self.some_int, some_list_of_obj, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new
print()