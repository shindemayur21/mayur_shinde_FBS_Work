# 7. Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit.

li = [ele for ele in range(1, 1001) 
          if any(ele % d == 0 for d in range(2, 10))]

print(li)