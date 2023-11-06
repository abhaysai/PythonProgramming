import unittest
from child_class_2 import ChildClass2

class TestChildClass2(unittest.TestCase):

    def test_child2_method(self):
        child2 = ChildClass2("Alice")
        child2.child2_method()
        self.assertEqual(child2.name, "Alice")

    def test_parent_method(self):
        child2 = ChildClass2("Bob")
        child2.parent_method()
        self.assertEqual(child2.name, "Bob")
    
    def test_init(self):
        child2 = ChildClass2("Charlie")
        self.assertEqual(child2.name, "Charlie")