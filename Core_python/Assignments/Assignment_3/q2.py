# Write a program to input any alphabet and check whether it is vowel or consonant.

char = str(input("Enter any character : "))

# if(char == 'A' or char == 'a' or char == 'E' or char == 'e' or char == 'I' or char == 'i' or char == 'O' or char == 'o' or char == 'U' or char == 'u'):
if char in ['A','a','E','e','I','i','O','o','U','u']:
    print("It is a vowel")
else:
    print("It is a Consonant")