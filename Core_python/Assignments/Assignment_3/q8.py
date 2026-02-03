# Write a program to prompt user to enter userid and password.
# After verifying userid and password display a 4 digit random number and ask user to enter the same.
# If user enters the same number then show him success message otherwise failed. (Something like captcha)

username = "mayurshinde12"
pswd = "ms1234"

print("To login in system please enter username & password :")

usr = str(input("Username : "))
pd = str(input("Password : "))

rdnum = id(usr)
if (username == usr and pswd == pd):
    print(f'Captcha : {rdnum}')
    usrcpt = int(input("Enter any for digits in sequence from captcha : "))
    if str(usrcpt) in str(rdnum):
        print("Logic successfull")
    else:
        print("Wrong captcha")
else:
    print("Invalid credentials")