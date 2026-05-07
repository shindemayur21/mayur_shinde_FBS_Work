st = 'I aM From Pune'

temp = ''

for i in range(len(st)):
    if st[i].isupper():
        temp = temp + st[i].lower()
    else:
        temp = temp + st[i].upper()

print(temp)
