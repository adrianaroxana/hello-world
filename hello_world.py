
def hello_world():
    return "Hello, World!"


def hello(name):
    if not name:
        return "Hello, World!"
    else:
        return "Hello" + ", " + name + "!"


def print_hello(name):
    if not name:
        print(hello(""))
    else:
        print(hello(name))


name = input("What is your name?")
print(hello_world())
print(hello(name))
print(hello(""))
print_hello(name)
print_hello("")
