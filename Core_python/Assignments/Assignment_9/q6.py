# 6. Write a program to print fibSeries series using recursion.

def fibSeries(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibSeries(n - 1) + fibSeries(n - 2)


num = int(input("Enter number of series: "))

# to print fibonacci series
print("fibSeries series:")
for i in range(num):
    print(fibSeries(i), end=" ")
