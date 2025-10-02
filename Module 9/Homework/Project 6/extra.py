# classes a, b, c
# a is parent of b
# b is parent of c

class A:
    def __init__(self):
        print("I am the parent of B and the grandparent of C")

class B(A):
    def __init__(self):
        super().__init__()
        print("I am the child of A and the parent of C")

class C(B):
    def __init__(self):
        super().__init__()
        print("I am the child of B and the grandchild of A")

x = C()