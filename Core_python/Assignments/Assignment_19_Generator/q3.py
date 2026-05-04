# Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def range_generator(srt, stop, stp):
    n = srt

    while (n < stop):
        yield n
        n += stp


start = int(input("Enter start : "))
stop = int(input("Enter stop : "))
step = int(input("Enter step : "))

for num in range_generator(start, stop, step):
    print(num)
