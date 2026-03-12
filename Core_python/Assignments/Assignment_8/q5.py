# 5. Sum of all prime numbers between 1 to n

def prime(n):
    sum = 0

    for m in range(2, n+1):

        for i in range(2, m):
            if (m % i == 0):
                break
        else:
            sum = sum + m

    return sum

num = int(input("Ente range : "))
print(f'Sum of all prime no between 1 to {num} : {prime(num)}')
