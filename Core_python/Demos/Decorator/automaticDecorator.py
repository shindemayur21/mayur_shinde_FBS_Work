def myDecorator(fun):
    def wrapper():
        print("This is wrapper function")
        fun()
        print("This is wrapper function")
    return wrapper


@myDecorator
def greet():
    print("Hello")


greet()
