#Check no is palindrome or not for 3 digits

ogNum = int(input("Enter any 3 digit number : "))

dig1 = (ogNum // 100)
dig2 = ((ogNum // 10) % 10) * 10
dig3 = (ogNum % 10) * 100

revNo = dig3 + dig2 + dig1

print(f'Original No : {ogNum}')
print(f'Reversed No : {revNo}')

#If original no equals(same) to reverse no, It will return True else False
print(revNo == ogNum) # comparing revNo with ogNum