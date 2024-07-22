import unittest

from ds.arraylist import StringArrayList
from ds.linked_list import GenericLinkedList, StringLinkedList, IntegerLinkedList, SizeError
# from ds.stack import IntegerStack, SizeError, StringStack


class StringArrayListTests(unittest.TestCase):

    def test_empty(self):
        arrayList = StringArrayList()
        self.assertTrue(arrayList.is_empty())
        self.assertEqual(arrayList.size, 0)

    def test_general_case(self):
        arrayList = StringArrayList()

        for i in range(9):
            arrayList.add(str(i))

        arrayList.add('69')
        self.assertFalse(arrayList.is_empty())

        for i in range(9):
            self.assertEqual(arrayList.remove(0), str(i))
            self.assertFalse(arrayList.is_empty())

        self.assertEqual(arrayList.remove(0), "69")
        self.assertTrue(arrayList.is_empty())

    def test_empty_removal(self):
        arrayList = StringArrayList()
        self.assertRaises(IndexError, arrayList.remove, 5)

    def test_get_error(self):
        arrayList = StringArrayList()
        self.assertRaises(IndexError, arrayList.get, 0)

    def test_get_indices(self):
        arrayList = StringArrayList()
        for i in range(5):
            arrayList.add(str(i))
        
        for i in range(3):
            self.assertEqual(arrayList.get(i), str(i))

    def test_get_invalid(self):
        arrayList = StringArrayList()

        arrayList.add('1')

        self.assertRaises(IndexError, arrayList.get, -1)
        self.assertRaises(IndexError, arrayList.get, 1)

    def test_remove_invalid(self):
        arrayList = StringArrayList()

        arrayList.add('1')

        self.assertRaises(IndexError, arrayList.remove, -1)
        self.assertRaises(IndexError, arrayList.remove, 1)
        
class StackTest(unittest.TestCase):
    
    def test_general_case(self):
        stack = StringStack(initial_size=100)
        self.assertTrue(stack.is_empty())

        # Go forward
        for i in range(100):
            stack.push(str(i))
            self.assertFalse(stack.is_empty())

        # Go in reverse
        for i in range(99, -1, -1):
            self.assertFalse(stack.is_empty())
            self.assertEqual(stack.peek(), str(i))
            self.assertEqual(stack.pop(), str(i))

        self.assertTrue(stack.is_empty())

    def test_out_of_bounds(self):

        with self.assertRaises(SizeError):
            stack = StringStack(10)
            self.assertTrue(stack.is_empty())

            # Add too much to crash
            for i in range(100):
                stack.push(str(i))
                self.assertFalse(stack.is_empty())
    
    def test_errors(self): # testing errors raise properly
        
        # Popping stacks
        with self.assertRaises(SizeError):
            stack = StringStack(initial_size=5)
            self.assertTrue(stack.is_empty())
            for i in range(5):
                stack.push(str(i))
                self.assertFalse(stack.is_empty())
            # popping stack till crash
            for i in range(100):
                stack.pop()
        
        # Peeking empty stack
        with self.assertRaises(SizeError):
            stack = StringStack(initial_size=5)
            self.assertTrue(stack.is_empty())
            stack.peek()
        
    
    def test_duplicate_elements(self): # do duplicate elements get removed properly
        stack = StringStack(initial_size=5)
        self.assertTrue(stack.is_empty())
        
        for i in range(5):
            stack.push("duplicate")
            self.assertFalse(stack.is_empty())
            self.assertEqual(stack.peek(), "duplicate")
        
        for i in range(5):
            self.assertFalse(stack.is_empty())
            self.assertEqual(stack.pop(), "duplicate")       
        
        self.assertTrue(stack.is_empty()) 

    def test_general_case_integers(self):
        stack = IntegerStack(initial_size=100)
        self.assertTrue(stack.is_empty())

        # Go forward
        for i in range(100):
            stack.push(i)
            self.assertFalse(stack.is_empty())

        # Go in reverse
        for i in range(99, -1, -1):
            self.assertFalse(stack.is_empty())
            self.assertEqual(stack.peek(), i)
            self.assertEqual(stack.pop(), i)

        self.assertTrue(stack.is_empty())

    def test_push_peek_jz(self):
        stack = StringStack(initial_size=5)
        self.assertTrue(stack.is_empty())
        self.assertRaises(SizeError, stack.peek)

        stack.push("Item 1")
        self.assertEqual(stack.size, 1)
        self.assertEqual(stack.peek(), "Item 1")
        self.assertFalse(stack.is_empty())

        stack.push("Item 2")
        stack.push("Item 3")
        self.assertEqual(stack.size, 3)
        self.assertEqual(stack.peek(), "Item 3")

        stack.push("Item 4")
        stack.push("Item 5")
        self.assertRaises(SizeError, stack.push, "Item 6")

    def test_pop_jz(self):
        stack = IntegerStack(initial_size=10000)
        self.assertTrue(stack.is_empty())
        self.assertRaises(SizeError, stack.pop)

        for i in range(10000):
            stack.push(i)

        self.assertFalse(stack.is_empty())

        self.assertEqual(stack.pop(), 9999)
        self.assertEqual(stack.size, 9999)
        self.assertEqual(stack.peek(), 9998)

        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.pop(), 5)

        for _ in range(9999):
            stack.pop()

        self.assertRaises(SizeError, stack.pop)


class LinkedListTest(unittest.TestCase):

    def test_empty(self):
        linked_list = StringLinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

    def test_general_case(self):

        class Circuit:
            voltage: float
            current: float

            def __init__(self, voltage: float, current: float):
                self.voltage = voltage
                self.current = current

            def resistance(self) -> float:
                return (self.voltage / self.current)

        linked_list = GenericLinkedList[Circuit]()

        for i in range(500, 2000, 50):
            new_circuit = Circuit(i * 2.0, i)
            linked_list.addEnd(new_circuit)

        while not linked_list.is_empty():
            circuit = linked_list.removeStart()
            self.assertEqual(circuit.resistance(), 2.0)

        for i in range(1, 2000):
            new_circuit = Circuit(i * 4.0, i)
            linked_list.addStart(new_circuit)

        while not linked_list.is_empty():
            circuit = linked_list.removeEnd()
            self.assertEqual(circuit.resistance(), 4.0)

        for i in range(1, 2000):
            new_circuit = Circuit(i * 10.0, i)
            linked_list.addStart(new_circuit)

        for i in range(1, 2000):
            new_circuit = Circuit(i * 20.0, i)
            linked_list.set(new_circuit, i - 1)

        for i in range(0, 1999):
            new_circuit = linked_list.get(i)
            self.assertEqual(new_circuit.resistance(), 20.0)


    def test_adding_jz(self):
        linked_list = IntegerLinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        for i in range(100):
            linked_list.addEnd(i)
            self.assertEqual(linked_list.get(i), i)
            self.assertEqual(linked_list.size, i + 1)

        for i in range(100):
            linked_list.addStart(i)
            self.assertEqual(linked_list.get(0), i)
            self.assertEqual(linked_list.size, i + 101)

        linked_list.add(1000, 100)
        self.assertEqual(linked_list.size, 201)
        self.assertEqual(linked_list.get(100), 1000)
        self.assertEqual(linked_list.get(99), 0)
        self.assertEqual(linked_list.get(101), 0)

        self.assertRaises(IndexError, linked_list.add, 1000, 202)
        self.assertRaises(IndexError, linked_list.add, 1000, -1)

        linked_list.add(1000, 201)
        self.assertEqual(linked_list.get(201), 1000)
        self.assertEqual(linked_list.size, 202)


    def test_get_set_jz(self):
        linked_list = IntegerLinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)
        self.assertRaises(IndexError, linked_list.get, 0)

        for i in range(100):
            linked_list.addEnd(1)
            self.assertEqual(linked_list.get(i), 1)

        self.assertRaises(IndexError, linked_list.get, -1)

        for i in range(100):
            self.assertEqual(linked_list.set(100, i), 1)
            self.assertEqual(linked_list.get(i), 100)
            self.assertEqual(linked_list.size, 100)

        self.assertRaises(IndexError, linked_list.set, 1000, 100)
        self.assertRaises(IndexError, linked_list.set, 1000, -1)


    def test_removing_jz(self):
        linked_list = IntegerLinkedList()
        self.assertTrue(linked_list.is_empty())
        self.assertEqual(linked_list.size, 0)

        self.assertRaises(SizeError, linked_list.removeEnd)
        self.assertRaises(SizeError, linked_list.removeStart)
        self.assertRaises(IndexError, linked_list.remove, 0)
        self.assertRaises(SizeError, linked_list.removeVal, 0)

        for i in range(100):
            linked_list.addEnd(i)

        for i in range(25):
            self.assertEqual(linked_list.removeEnd(), 99 - i)

        self.assertEqual(linked_list.size, 75)

        for i in range(25):
            self.assertEqual(linked_list.removeStart(), i)

        self.assertEqual(linked_list.size, 50)

        self.assertEqual(linked_list.remove(25), 50)
        self.assertEqual(linked_list.get(24), 49)
        self.assertEqual(linked_list.get(25), 51)
        self.assertEqual(linked_list.size, 49)

        self.assertRaises(IndexError, linked_list.remove, 49)
        self.assertRaises(IndexError, linked_list.remove, -1)

        linked_list = IntegerLinkedList()

        for i in range(100):
            linked_list.addEnd(i)

        self.assertEqual(linked_list.is_empty(), False)
        
        self.assertEqual(linked_list.removeVal(5), 5)
        self.assertEqual(linked_list.size, 99)
        self.assertEqual(linked_list.get(5), 6)
        self.assertEqual(linked_list.get(4), 4)
        self.assertEqual(linked_list.removeVal(101), None)
    
class QueueTest(unittest.TestCase):
    def test_queue_ll(self):
        test_ll = StoreLineLL()
        test_list = ["John","Jim","Jerry","Jack","Jimmy"]
        test_ll.enqueue("John")
        test_ll.enqueue("Jim")
        test_ll.enqueue("Jerry")
        test_ll.enqueue("Jack")
        test_ll.enqueue("Jimmy")

        current = test_ll.list.head
        i = 0
        check_full = True
        while current != None:
            if current.val.name != test_list[i]:
               check_full = False
            current = current.next
            i+=1
        
        self.assertTrue(check_full)

        test_ll.dequeue()
        test_ll.dequeue()
        test_list = ["Jerry","Jack","Jimmy"]
        current = test_ll.list.head
        i = 0
        check_part = True
        while current != None:
            if current.val.name != test_list[i]:
               check_part = False
            current = current.next
            i+=1
        
        self.assertTrue(check_part)

        self.assertTrue(test_ll.peek() == "Jerry")

        test_ll.dequeue()
        test_ll.dequeue()
        test_ll.dequeue()
        test_ll.dequeue()
        test_ll.dequeue()
        test_ll.dequeue()

        self.assertTrue(test_ll.list.is_empty())



    def test_queue_array(self):
        test_qa = StoreLineArray()
        test_list = ["John","Jim","Jerry","Jack","Jimmy","Jeremiah","Jeremy","Jan","Jill","Jonny","Jobe"]
        for i in range(0,len(test_list)):
            test_qa.enqueue(test_list[i])
        
        check_full = True
        for i in range(0,len(test_qa.array)):
            if(test_qa.array[i].name != test_list[i]):
                check_full = False
        
        self.assertTrue(check_full)

        test_qa.dequeue()
        test_qa.dequeue()
        test_qa.dequeue()
        test_qa.dequeue()
        test_qa.dequeue()
        test_qa.dequeue()

        self.assertTrue(test_qa.peek() == "Jeremy")

        test_list = ["Jeremy","Jan","Jill","Jonny"]

        check_part = True
        for i in range(0,4):
            if test_qa.array[i].name != test_list[i]:
                check_part = False
        for i in range(4, len(test_qa.array)):
            if test_qa.array[i] != None:
                check_part = False
        
        self.assertTrue(check_part)

        test_qa.dequeue()
        test_qa.dequeue()
        test_qa.dequeue()
        test_qa.dequeue()
        test_qa.dequeue()
        test_qa.dequeue()
        self.assertTrue(test_qa.array == [None,None,None,None,None,None,None,None,None,None])
        
    def test_queue_double_stack(self):
        test_ds = StoreLineDoubleStack()
        test_list = ["John","Jim","Jerry","Jack","Jimmy","Jeremiah","Jeremy","Jan","Jill","Jonny","Jobe"]
        for i in range(0,len(test_list)):
            test_ds.enqueue(test_list[i])

        check_full = True
        for i in range (0,len(test_ds.stack1.stack)):
            if(test_ds.stack1.stack[i].name != test_list[9-i]):
                check_full = False
        self.assertTrue(check_full)

        test_ds.dequeue()
        test_ds.dequeue()
        test_ds.dequeue()
        test_ds.dequeue()
        test_ds.dequeue()
        test_ds.dequeue()
        
        self.assertTrue(test_ds.peek().name == "Jeremy")

        test_list = ["Jeremy","Jan","Jill","Jonny"]

        check_part = True
        for i in range(0,6):
            if test_ds.stack2.stack[i] != None:
                check_part = False
        for i in range(6, 10):
            if test_ds.stack2.stack[i].name != test_list[i-6]:
                check_part = False

        self.assertTrue(check_part)

        test_ds.dequeue()
        test_ds.dequeue()
        test_ds.dequeue()
        test_ds.dequeue()
        test_ds.dequeue()
        test_ds.dequeue()

        self.assertTrue(test_ds.stack1.stack == [None,None,None,None,None,None,None,None,None,None])
        self.assertTrue(test_ds.stack2.stack == [None,None,None,None,None,None,None,None,None,None])


if __name__ == "__main__":
    unittest.main()
