import unittest 
from child_class_1 import ChildClass1

class TestChildClass1(unittest.TestCase):

    def test_child1_method(self):
        child1 = ChildClass1("Jane")
        child1.child1_method()
        self.assertEqual(child1.name, "Jane")
    
    def test_parent_method(self):
        child1 = ChildClass1("Joe")
        child1.parent_method()
        self.assertEqual(child1.name, "Joe")

    def test_init(self):
        child1 = ChildClass1("Maria")
        self.assertEqual(child1.name, "Maria")
