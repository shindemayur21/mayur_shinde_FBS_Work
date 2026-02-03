# Write a program to check if user has entered correct userid and password.

username = "mayurshinde12"
pswd = "ms1234"

print("To login in system please enter username & password :")

usr = str(input("Username : "))
pd = str(input("Password : "))

if (username == usr and pswd == pd):
    print("Logic successfull")
else:
    print("Invalid credentials")