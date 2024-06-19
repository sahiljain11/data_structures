'''
    Do NOT read this file unless you have already completed the assignment!
    You learning by DOING not cheating!!!
'''

from typing import Generic, TypeVar


class SizeError(Exception):
    pass

T = TypeVar('T')
class GenericStack(Generic[T]):

    # The size of the stack should never change!!
    def __init__(self, initial_size: int = 10) -> None:
        self.stack = [None] * initial_size
        self.size = 0

    def pop(self) -> T:
        '''
            Remove the top element from the stack AND return the value
        '''
        removed = self.peek()
        self.size -= 1
        return removed

    def push(self, val: T) -> None:
        '''
            Push a new value at the top of the stack
        '''
        if self.size == len(self.stack):
            raise SizeError("Stack is full.")
        
        self.stack[self.size] = val
        self.size += 1

    def peek(self) -> T:
        '''
            Returns the value at the top of the stack but does NOT remove
            it from the stack
        '''
        if self.is_empty():
            raise SizeError("Stack is empty.")
        
        return self.stack[self.size - 1]

    def is_empty(self) -> bool:
        '''
            Returns true if the stack has no elements
        '''
        return self.size == 0


class StringStack(GenericStack[str]):
    pass

class IntegerStack(GenericStack[int]):
    pass