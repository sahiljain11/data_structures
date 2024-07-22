from typing import Generic, TypeVar
from stack import GenericStack as Stack
from linked_list import GenericLinkedList as LinkedList

""" You are an owner of a hot dog stand (vegetarian hot dogs for Blaze and GameBot).
All of a sudden aliens take over the planet and capture the entire planet. They
are about to destroy your hot dog stand when they notice how good your (vegetarian)
hot dogs are. Because of this, they make a bet with you: Simulate your hotdog stand
business using python code, and if you pass, humanity will be saved. Because you're
an overachiever (nerd), you want to implement this not only by using a Linked List
but ALSO USING AN IMMUTEABLE ARRAY OF SIZE 10 AND USING TWO STACKS. 
Good luck, the fate of humanity lies in your hands.
"""

T = TypeVar('T')
class Person(Generic[T]):

    def __init__(self,name) -> None:
        self.name = name
        


class StoreLineLL(Generic[T]):

    def __init__(self) -> None:

        self.list = LinkedList[T]()


    def enqueue(self, new_name: T) -> None:

        """ Write an enqueue that works with linked lists """

        pass


    def dequeue(self) -> T:

        """ Write a dequeue that works with LL
        Should return a Person """

        pass

    def peek(self) -> T:

        """ NEW FUNCTION see if you can add a peek for LL to see whos at the front of the line
        Should return a Person """

        pass


class StoreLineArray(Generic[T]):

    """ HEHEHEHEHEHEHEHE Challenge Mode """

    def __init__(self, size: int = 10) -> None:
        self.array = [None] * size          

    """instantiate empty list of size 10 DO NOT CHANGE THE SIZE
    think about how you can keep track of the front and the rear 
    of the queue without changing the size of the array"""

    def enqueue(self, new_name: T) -> None:

        """ Write Dis """
        
        pass

    def dequeue(self) -> T:
        
        """ Write Dis """

        pass

    def peek(self) -> T:

        """ Write Dis """

        pass
    
class StoreLineDoubleStack(Generic[T]):

    """ CHALLENGE MODE PART 2
    Rather than modifying our stack functions like we did above,
    How can we implement a queue using 2 Stacks without modifying the stack funcs?
    """

    def __init__(self) -> None:
        self.stack1 = Stack[T]()
        self.stack2 = Stack[T]()

            
    def enqueue(self, new_name: T) -> None:

        """ Write Dis """
            
        pass
        
    def dequeue(self) -> T:
            
        """ Write Dis """
            
        pass
        
    def peek(self) -> T:
            
        """ Write Dis """
            
        pass


    

    
