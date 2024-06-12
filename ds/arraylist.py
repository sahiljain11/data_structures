
from typing import Generic, TypeVar

T = TypeVar('T')
class ArrayList(Generic[T]):

    def __init__(self, initial_size: int = 10) -> None:
        self.arr = [None] * initial_size
        self.size = 0

    def add(self, value: T) -> None:
        pass

    def remove(self, idx: int) -> T:
        pass

    def get(self, idx: int) -> T:
        pass

    def is_empty(self) -> bool:
        pass

class StringArrayList(ArrayList[str]):
    pass