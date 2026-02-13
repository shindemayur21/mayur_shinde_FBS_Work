n = int(input("Enter a 3 digit number : "))

fd = n // 100        # firsr digit
sd = (n // 10) % 10  # second digit
td = n % 10          # third digit

if (sd*2 == fd) and (td//2 == fd):
    print("Yes, you have done it")
else:
    print("Please try next time")