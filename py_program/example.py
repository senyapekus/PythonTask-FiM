def function1(arg1, arg2, arg3):
    print(arg3)


def function2():
    print("Hello, I'm without arguments")


if __name__ == '__main__':
    hello = 3
    raritu = []
    raritu.append("cake")
    raritu.append("cookie")
    if hello == "Hello world":
        while hello > 2:
            print("Hello is hello world")
        print("priv")
    elif hello != 3:
        food = raritu[0]
        print("elif")
    else:
        # this is else block
        function2()
        function1("Steve", "Mary", "Lada")
        hello *= 15
        print("Hello is not hello world")
        hello -= 2
    print(hello)
    print(raritu[0])
