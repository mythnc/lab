def foo():
    raise Exception('error in foo')

def main():
    try:
        return foo()
    except Exception:
        return None
    finally:
        print('always execute')


if __name__ == "__main__":
    print(main())