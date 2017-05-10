class TestPython:

    def __init__(self,name):
        self.name=name

    def j(self):
        return "test from function"

x=TestPython("Test Class")

print(x.name)
print(x.j())


