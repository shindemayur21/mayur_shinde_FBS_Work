# 5. Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

def linearSearch(li, search_ele):
    count = 0
    first_index = -1
    
    for i in range(len(li)):
        if li[i] == search_ele:
            count += 1
            if first_index == -1:  # store first occurrence
                first_index = i
    
    return first_index, count


li = [23, 65, 2, 10, 817, 425, 2, 9]
ele = int(input("Enter element to search: "))

index, occ = linearSearch(li, ele)

if index != -1:
    print(f"{ele} present at index {index} and occurs {occ} times")
else:
    print(f"{ele} not present")
