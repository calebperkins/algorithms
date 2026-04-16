from collections import OrderedDict
from typing import Mapping, TypeVar

Key = TypeVar("Key")
Value = TypeVar("Value")


class LRUCache(Mapping[Key, Value]):
    def __init__(self, capacity: int):
        assert capacity > 0
        self._capacity = capacity
        self._data: OrderedDict[Key, Value] = OrderedDict()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key: Key) -> Value:
        self._data.move_to_end(key)
        return self._data[key]

    def __setitem__(self, key: Key, value: Value) -> None:
        if key not in self._data and len(self._data) == self._capacity:
            self._data.popitem(last=False)
        self._data[key] = value
        self._data.move_to_end(key)
