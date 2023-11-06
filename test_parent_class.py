import unittest
from parent_class import ParentClass

class TestParentClass(unittest.TestCase):

    def test_parent_method(self):
        parent = ParentClass("John")
        parent.parent_method()
        self.assertEqual(parent.name, "John")