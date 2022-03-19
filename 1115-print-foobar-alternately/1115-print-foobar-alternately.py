from threading import Condition

class FooBar:
    def __init__(self, n):
        self.n = n
        self.cv = Condition()
        self.f = 0
        self.fdone = lambda: self.f == 1
        self.bdone = lambda: self.f == 0

    def foo(self, printFoo: "Callable[[], None]") -> None:

        for i in range(self.n):
            with self.cv:
                self.cv.wait_for(self.bdone)
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.f = 1
                self.cv.notify_all()

    def bar(self, printBar: "Callable[[], None]") -> None:

        for i in range(self.n):
            with self.cv:
                self.cv.wait_for(self.fdone)
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.f = 0
                self.cv.notify_all()