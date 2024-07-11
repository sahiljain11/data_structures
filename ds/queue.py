from typing import Generic, TypeVar

""" You are an owner of a hot dog stand (vegetarian hot dogs for Blaze and GameBot).
All of a sudden aliens take over the planet and capture the entire planet. They
are about to destroy your hot dog stand when they notice how good your (vegetarian)
hot dogs are. Because of this, they make a bet with you: Simulate your hotdog stand
business using python code, and if you pass, humanity will be saved. Because you're
an overachiever (nerd), you want to implement this not only by modifying your old
stack code but ALSO USING AN IMMUTEABLE ARRAY OF SIZE 10 AND USING TWO STACKS. 
Good luck, the fate of humanity lies in your hands.
"""

T = TypeVar('T')
class Person(Generic[T]):

    def __init__(self,name) -> None:
        self.name = name


class StoreLineStack(Generic[T]):

    def __init__(self) -> None:

        """ implement your stack here """

        pass

    def enqueue(self, new_name: T) -> None:

        """ Rewrite one of your stack functions to work here """

        pass


    def dequeue(self) -> T:

        """ Rewrite one of your stack functions to work here
        ALSOOO Modify the dequeue so it returns the person that got dequeued
        Should return a Person """

        pass

    def peek(self) -> T:

        """ NEW FUNCTION see if you can modify your stack peek code to see whos at the front of the line
        Should return a Person """

        pass


class StoreLineArray(Generic[T]):

    """ HEHEHEHEHEHEHEHE Challenge Mode """

    def __init__(self) -> None:
        self.array = [None] * 10          #instantiate empty list of size 10 DO NOT CHANGE THE SIZE

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

        """ Write Dis """

        pass
            
    def enqueue(self, new_name: T) -> None:
        
        """ Write Dis """
            
        pass
        
    def dequeue(self) -> T:
            
        """ Write Dis """
            
        pass
        
    def peek(self) -> T:
            
        """ Write Dis """
            
        pass


    

    
