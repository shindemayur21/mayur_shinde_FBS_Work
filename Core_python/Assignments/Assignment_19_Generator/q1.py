# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fib_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


num = int(input("Enter a number of series : "))
gen = fib_gen(num)

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
