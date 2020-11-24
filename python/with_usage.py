from contextlib import contextmanager
import time


class Indenter():
    def __init__(self):
        self.indent_times = 0
        self.indent_space = 4

    def __enter__(self):
        self.indent_times += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent_times -= 1

    def print(self, str_):
        indent = ' ' * self.indent_space * (self.indent_times - 1)
        print('{}{}'.format(indent, str_))


def use_with_as_an_indenter():
    with Indenter() as indent:
        indent.print('hi!')
        with indent:
            indent.print('hello')
            with indent:
                indent.print('bonjour')
        indent.print('hey')


class TimeTrack:
    def __init__(self):
        self.start = 0.0
        self.end = 0.0

    def __enter__(self):
        print('start')
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print('end')
        print(self.end - self.start)


@contextmanager
def time_tracker():
    try:
        start = time.time()
        yield start
    finally:
        end = time.time()
        print(end - start)


if __name__ == "__main__":
    with time_tracker():
        time.sleep(1000 * 10)
