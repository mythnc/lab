class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


def repeater(value):
    while True:
        yield value


def bounded_repeater(value, max_repeats):
    for _ in range(max_repeats):
        yield value


for x in bounded_repeater('hello', 2):
    print(x)

# repeater = Repeater('hello')
# for item in repeater:
#     print(item)

# repeater = BoundedRepeater('hello', 3)
# for item in repeater:
#     print(item)
    