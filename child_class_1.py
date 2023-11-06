from parent_class import ParentClass

class ChildClass1(ParentClass):
    def __init__(self, name):
        super().__init__(name)
    
    def child1_method(self):
        print("Child 1 method called")