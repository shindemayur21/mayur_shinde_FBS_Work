loc = ['s1', 's2', 's3', 's4', 's5', 's6']
dist = [2500, 1800, 1000, 2300, 3700, 600]

# sum of all distance
# total = sum(dist)

src = input("Enter destination one : ")  # destination 1
dest = input("Enter destination two : ")  # destination 2

ind1 = loc.index(src)   # to get the index of destination 1
ind2 = loc.index(dest)   # to get the index of destination 2

i = ind1
tot_dist = 0
while(i != ind2):
    tot_dist = tot_dist + dist[i]
    if(i == len(loc) - 1):
        i = 0 
    # else:
    #     i += 1

print(tot_dist)

cost_km = float(input("Enter cost per km : "))
cost = (tot_dist /1000) * cost_km
print(f'Total cost : {cost}')