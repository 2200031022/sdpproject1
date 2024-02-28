class MyClass:
    def __init__(self, name):
        self.name = name

    def display_namespace(self):
        print("Namespace of MyClass:", vars(self))

obj = MyClass("Example")
obj.display_namespace()
