class A:
    def __init__(self):
        self.a='a'
        print(self.a)


class B:
    def __init__(self):
        self.b='b'
        print(self.b)


class C (A,B):  #here its printing c,a as first control goes to class C then as super is ther it will go to class A also as traverse path is A,B, from left side
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()

o=C()

#to over come above problem as its not travrsng to class B, define super() method in all classes

print("to over come above problem as its not travrsng to class B, define super() method in all classes")
class A:
    def __init__(self):
        self.a='a'
        print(self.a)
        super().__init__()

class B:
    def __init__(self):
        self.b='b'
        print(self.b)
        super().__init__()

class C (A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()

o=C()