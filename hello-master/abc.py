class A:
    def a(self, i):
        return i * 2

class AA:
    def a(self, i):
        return i * 3

class B(AA, A):
    def b(self, i):
        return i * 4

class C(B):
    def b(self, i):
        return i * 8

c = C()

print(c.a(2))
# print(c.aa(2))
