def greet():
    print('Good Afternoon..!')


def myDecorator(fun):  # fun = greet
    print('Decorator started')
    fun()
    print('Decorator ended')


myDecorator(greet)
