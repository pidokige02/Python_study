
class TestClass:
    name = "TEST"

    def __init__(self):
        print("TTTTTTTTTTTTTT")

    @staticmethod       #static method 가 아닌것도 강제로 static method 로 만들어 버림.
    def static_method():
        print("STATIC!!")

    def set_name(self, new_name):
        self.name = new_name
        print("SET NAME>>", self.full_name)

    @property           #full_name() 대신 full_name 과 같이 호출이 가능하다. 
    def full_name(self):
        return self.name + " FFFF"

    def get_name(self):
        print("QQQQQQQQQQQQQQQQQQQQ")
        return self.name

    def area(self, x, y):
        return x * y

class Child(TestClass):
    def __init__(self):
        super().__init__()
        print("My init!!!")

    def get_name(self):
        t = super().get_name()
        return "Child Name:" + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t / 2

test = TestClass()
child = Child()

test.static_method()
TestClass.static_method()

print("FFFFFFF>>", test.full_name)
test.set_name("RRRRRRRRRRRRrdd")
print("FFFFFFF>>", test.full_name)

print(test.static_method)       # instance로 static method 를 호출함 @staticmethod 때문에 가능한 것임.
                                # static method 는 일반적으로 class name 으로만 가능한것임.
print(TestClass.static_method)

cmd = input("Input the function name>> ")

# getattr(test, cmd)()
# getattr(TestClass, 'static_method')()

# print("11111>>", child.get_name())

# c = callable(test.get_name)
# print("cccccccc>>", c)
