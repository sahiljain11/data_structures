'''
    Do NOT read this file unless you have already completed the assignment!
    You learning by DOING not cheating!!!
'''

from typing import Generic, TypeVar

T = TypeVar('T')
class ArrayList(Generic[T]):

    def __init__(self, initial_size: int = 10) -> None:
        self.arr = [None] * initial_size
        self.size = 0

    def add(self, value: T) -> None:
        if self.size == len(self.arr):
            arr2 = [None] * self.size * 2

            for i in range(len(self.arr)):
                arr2[i] = self.arr[i]
            
            self.arr = arr2

        self.arr[self.size] = value
        self.size += 1

    def remove(self, idx: int) -> T:
        removed = self.get(idx)

        for i in range(idx, len(self.arr) - 1):
            self.arr[i] = self.arr[i+1]

        self.size -= 1
        return removed

    def get(self, idx: int) -> T:

        if idx < 0 or self.size <= idx:
            raise IndexError(f"Index does not exist: {idx}")
        
        return self.arr[idx]
    
    def set(self, val: T, idx: int) -> None:
        if idx < 0 or self.size <= idx:
            raise IndexError(f"Index does not exist: {idx}")
        
        self.arr[idx] = val

    def is_empty(self) -> bool:
        return self.size == 0

class StringArrayList(ArrayList[str]):
    pass