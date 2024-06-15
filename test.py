import unittest

from ds.arraylist import StringArrayList
from ds.stack import IntegerStack, SizeError, StringStack

class StringArrayListTests(unittest.TestCase):

    def test_empty(self):
        arrayList = StringArrayList()
        self.assertTrue(arrayList.is_empty())
        self.assertEqual(arrayList.size, 0)

    def test_whatever(self):
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
        stack = IntegerStack(initial_size=5)
        self.assertTrue(stack.is_empty())
        self.assertRaises(SizeError, stack.pop)

        for i in range(5):
            stack.push(i)

        self.assertFalse(stack.is_empty())

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.size, 4)
        self.assertEqual(stack.peek(), 3)

        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.pop(), 5)

        for i in range(4):
            stack.pop()

        self.assertRaises(SizeError, stack.pop)

if __name__ == "__main__":
    unittest.main()