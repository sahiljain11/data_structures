from typing import Generic, TypeVar


class SizeError(Exception):
    pass

T = TypeVar('T')
class GenericStack(Generic[T]):

    # The size of the stack should never change!!
    def __init__(self, initial_size: int = 10) -> None:
        self.stack = [''] * initial_size
        self.size = 0

    def pop(self) -> T:
        '''
            Remove the top element from the stack AND return the value
        '''
        pass

    def push(self, val: T) -> None:
        '''
            Push a new value at the top of the stack
        '''
        pass

    def peek(self) -> T:
        '''
            Returns the value at the top of the stack but does NOT remove
            it from the stack
        '''
        pass

    def is_empty(self) -> bool:
        '''
            Returns true if the stack has no elements
        '''
        pass


class StringStack(GenericStack[str]):
    pass

class IntegerStack(GenericStack[int]):
    pass