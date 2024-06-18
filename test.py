import unittest

from ds.arraylist import StringArrayList
from ds.linked_list import GenericLinkedList, StringLinkedList
from ds.stack import IntegerStack, SizeError, StringStack


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
            current: float
            resistance: float

            def __init__(self, current: float, resistance: float):
                self.current = current
                self.resistance = resistance

            def voltage(self) -> float:
                return (self.current / self.resistance)

        linked_list = GenericLinkedList[Circuit]()

        for i in range(500, 2000, 50):
            new_circuit = Circuit(i * 2.0, i)
            linked_list.addEnd(new_circuit)

        while not linked_list.is_empty():
            circuit = linked_list.removeStart()
            self.assertEqual(circuit.voltage(), 2.0)

        for i in range(0, 2000):
            new_circuit = Circuit(i * 4.0, i)
            linked_list.addStart(new_circuit)

        while not linked_list.is_empty():
            circuit = linked_list.removeEnd()
            self.assertEqual(circuit.voltage(), 4.0)

        for i in range(0, 2000):
            new_circuit = Circuit(i * 10.0, i)
            linked_list.addStart(new_circuit)

        for i in range(0, 2000):
            new_circuit = Circuit(i * 20.0, i)
            linked_list.set(new_circuit, i)

        for i in range(0, 2000):
            new_circuit = linked_list.get(i)
            self.assertEqual(circuit.voltage(), 20.0)


if __name__ == "__main__":
    unittest.main()