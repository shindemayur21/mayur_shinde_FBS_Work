# WAP to print Armstrong number between range

sn = int(input("Enter starting number for range : "))
ln = int(input("Enter last number for range : "))

for i in range(sn, ln+1):
    if(i in range(1, 10)): #integers from 1 to 9 are armstrong
        print(f'{i} is an Armstrong number')

    elif(i > 9):
        cnt = 0
        for _ in str(i):
            cnt += 1

        j = i
        arm = 0
        while(i > 0): # 153, 15, 1
            d = i % 10 # 3, 5, 1
            arm = arm + (d ** cnt)
            i = i // 10
            
        if(arm == j):
            if (arm >= sn and arm <= ln):
                print(f'{arm} is an Armstrong number')