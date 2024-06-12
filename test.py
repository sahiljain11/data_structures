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


if __name__ == "__main__":
    unittest.main()