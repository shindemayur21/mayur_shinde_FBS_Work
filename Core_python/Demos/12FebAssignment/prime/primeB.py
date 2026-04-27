# print first 20 prime nos
n = int(input("Enter a number for range : "))

cnt = 0
for num in range(2, n+1):
    for i in range(2, num):
        if (num % i == 0):
            break
    else:
        cnt += 1
        print (f'Prime number {cnt} : {num}')
        if(cnt == 20):
            break