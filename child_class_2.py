from parent_class import ParentClass  

class ChildClass2(ParentClass):
    def __init__(self, name):
        super().__init__(name)

    def child2_method(self):
        print("Child 2 method called")