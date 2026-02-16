# Write a program to prompt user to enter userid and password.
# If Id and password is incorrect give him chance to re-enter the credentials.
# Let him try 3 times. After that program to terminate.

username = "mayurshinde"
password = "ms1234"

cnt = 1
while (cnt <= 3):
    usr = str(input("Enter username : "))
    pswd = str(input("Enter password : "))

    if (username == usr and password == pswd):
        print("Login successful")
    else:
        print("Invalid credentials, Try again")
        print(f'{3 - cnt} attempt remaining')
    cnt += 1
    if (cnt > 3):
        print("Done with 3 attempts, Try after 24 hours...!")
        break
