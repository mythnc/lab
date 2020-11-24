def foo(required, *args, **kwargs):
    print(required)
    print(args is None)
    print(type(args))
    print(args)
    if args: print(args)
    if kwargs: print(kwargs)


def main():
    foo('hi')


if __name__ == "__main__":
    main()