from typing import Generic, TypeVar


class SizeError(Exception):
    pass

T = TypeVar('T')


class Node(Generic[T]):
    '''
        This class should NOT be called anywhere outside of the LinkedList class!!
    '''    
    def __init__(self, val: T, is_header: bool = False) -> None:
        self.val = val
        self.next: Node = None
        self.prev: Node = None


class GenericLinkedList(Generic[T]):


    # The size of the linked list should never change!!
    def __init__(self) -> None:
        self.header_node = Node(None, is_header=True)

    def addEnd(self, val: T) -> None:
        '''
            Add to the end of the linked list
        '''
        pass

    def addStart(self, val: T) -> None:
        '''
            Add to the beginning of the linked list
        '''
        pass

    def add(self, val: T, idx: int) -> None:
        '''
            Add at a specific index. If the current list is n elements long and
            the idx is greater n + 1, throw an error!
        '''
        pass

    def removeStart(self) -> T:
        '''
            Remove the first element in the linked list
        '''
        pass

    def removeEnd(self) -> T:
        '''
            Remove the last element in the linked list
        '''
        pass

    def remove(self, idx: int) -> T:
        '''
            Remove an element at a given index
        '''
        pass

    def get(self, idx: int) -> T:
        '''
            Get a value in the linkedlist
        '''
        pass

    def set(self, val: T, idx: int) -> T:
        '''
            Update a value in the linkedlist
        '''
        pass

    def is_empty(self) -> bool:
        '''
            Returns true if the linked list has no elements
        '''
        pass


class StringLinkedList(GenericLinkedList[str]):
    pass

class IntegerLinkedList(GenericLinkedList[int]):
    pass