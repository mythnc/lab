class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42

    def get_gg(self):
        return __gg


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden foo'
        self._bar = 'overridden _bar'
        self.__baz = 'overridden __baz'


def main():
    t2 = ExtendedTest()
    print(t2.foo)
    print(t2._bar)
    # print(t2.__baz)
    print(t2._ExtendedTest__baz)
    print(t2._Test__baz)


if __name__ == "__main__":
    _Test__gg = 'gg'
    print(Test().get_gg())
    main()