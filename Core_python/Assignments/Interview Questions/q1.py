dest = ['s1', 's2', 's3', 's4', 's5', 's6']
dist = [2500, 1800, 1000, 2300, 3700, 600]

# sum of all distance
total = sum(dist)

d1 = input("Enter destination one : ")  # destination 1
d2 = input("Enter destination two : ")  # destination 2

ind1 = dest.index(d1)   # to get the index of destination 1
ind2 = dest.index(d2)   # to get the index of destination 2

sum1 = 0

# if destination 1 index is higher than destination 2 index
if ind1 > ind2:
    for i in range(ind2+1, ind1+1):
        sum1 = sum1 + (dist[i])
    total = total - sum1
    print(f'Total distance is : {total}')

# if destination 2 index is higher than destination 1 index
else:
    for i in range(ind1+1, ind2+1):
        sum1 = sum1 + (dist[i])
    print(f'Total distance is : {sum1}')
