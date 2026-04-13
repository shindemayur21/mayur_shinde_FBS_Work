# 2. Python Program to Concatenate Two Dictionaries Into One.

di = {id:101,'name':'mayur'}
di2= {'add':'pune','dept':'IT'}

# Method 1
# di3 = di.copy()
# di3.update(di2)
# print(di3)

# Method 2
di3={**di,**di2}
print(di3)