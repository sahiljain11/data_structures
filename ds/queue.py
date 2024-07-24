from typing import Generic, TypeVar
from stack import GenericStack as Stack
from linked_list import GenericLinkedList as LinkedList

"""
    You are an owner of a hot dog stand (vegetarian hot dogs for Blaze and GameBot).
    All of a sudden aliens take over the planet and capture the entire planet. They
    are about to destroy your hot dog stand when they notice how good your (vegetarian)
    hot dogs are. Because of this, they make a bet with you: Simulate your hotdog stand
    business using python code, and if you pass, humanity will be saved. Because you're
    an overachiever (nerd), you want to implement this not only by using a Linked List
    but ALSO USING AN IMMUTEABLE ARRAY OF SIZE 10 AND USING TWO STACKS. 
    Good luck, the fate of humanity lies in your hands.
"""

T = TypeVar('T')


class Queue(Generic[T]):

    def __init__(self) -> None:
        self.list = LinkedList[T]()

    def enqueue(self, element: T) -> None:
        pass

    def dequeue(self) -> T:
        pass

    def peek(self) -> T:
        pass



class QueueLinkedList(Queue[T]):

    def __init__(self) -> None:
        self.list = LinkedList[T]()


    def enqueue(self, element: T) -> None:
        """
            This function should add the given element into the end of the queue.
            This should be O(1)
        """
        pass


    def dequeue(self) -> T:
        """
            This function should return the next element in the queue
            If there is no element, throw an error. This should be O(1)
        """

        pass

    def peek(self) -> T:
        """
            This function should return the next element in the queue.
            This should NOT remove any elements in the queue.
            If there is no element, throw an error. This should be O(1)
        """
        pass


class QueueArray(Queue[T]):

    def __init__(self, size: int = 10) -> None:
        """
            instantiate empty list of size 10 DO NOT CHANGE THE SIZE
            think about how you can keep track of the front and the rear 
            of the queue without changing the size of the array
        """
        self.array = [None] * size          


    def enqueue(self, element: T) -> None:
        """
            This function should add the given element into the end of the queue.
            If there is no space left, throw an error! This should be O(1)
        """
        pass

    def dequeue(self) -> T:
        """
            This function should return the next element in the queue
            If there is no element, throw an error. This should be O(1)
        """

        pass

    def peek(self) -> T:
        """
            This function should return the next element in the queue.
            This should NOT remove any elements in the queue.
            If there is no element, throw an error. This should be O(1)
        """
        pass
    
class QueueDoubleStack(Queue[T]):

    """ CHALLENGE MODE PART 2
        Rather than modifying our stack functions like we did above,
        How can we implement a queue using 2 Stacks without modifying the stack funcs?

        This is considered a bonus and OPTIONAL!!
    """

    def __init__(self) -> None:
        self.stack1 = Stack[T]()
        self.stack2 = Stack[T]()

            
    def enqueue(self, element: T) -> None:
        """
            This function should add the given element into the end of the queue.
            If there is no space left, throw an error! This should be O(1)
        """
        pass
        
    def dequeue(self) -> T:
        """
            This function should return the next element in the queue
            If there is no element, throw an error. This should be O(N) in the worst
            and average cases and O(1) in best case
        """
        pass
        
    def peek(self) -> T:
        """
            This function should return the next element in the queue.
            This should NOT remove any elements in the queue.
            If there is no element, throw an error. This should be O(N) in the worst
            and average cases and O(1) in best case
        """
        pass


    
class Person:
    def __init__(self, name: str) -> None:
        self.name = name


class StoreLineLinkedList(QueueLinkedList[Person]):
    pass

class StoreLineArray(QueueArray[Person]):
    pass

class StoreLineDoubleStack(QueueDoubleStack[Person]):
    pass
