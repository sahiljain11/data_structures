import unittest

from ds.arraylist import StringArrayList
from ds.stack import SizeError, StringStack

@unittest.SkipTest
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

# @unittest.SkipTest
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
    
    def test_push_pop(self): # testing pushing and popping 
        stack = StringStack(initial_size=10)
        self.assertTrue(stack.is_empty())
        
        stack.push("one")
        self.assertEqual(stack.peek(), "one")
        stack.push("two")
        self.assertEqual(stack.pop(), "two")
        self.assertEqual(stack.peek(), "one")
        
        stack.push("three")
        self.assertEqual(stack.pop(), "three")
        self.assertEqual(stack.peek(), "one")
        self.assertEqual(stack.pop(), "one")
        self.assertTrue(stack.is_empty())
    
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

if __name__ == "__main__":
    unittest.main()