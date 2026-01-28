#Convert the time entered in hh,min and sec into seconds.

hr = int(input("Enter hours : "))
mint = int(input("Enter minute : "))
sec = int(input("Enter seconds : "))

#Converting hrs into seconds
#first 60 to convert in minutes & 2nd to convert in seconds
hr_sec = hr * 60 * 60

#converting minute into seconds by multiplying by 60
min_sec = mint * 60

#converting into seconds
s_sec = sec * 1

print(f'Hours in seconds : {hr_sec}')
print(f'Minutes in seconds : {min_sec}')
print (f'Seconds in seconds : {s_sec}')