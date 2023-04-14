string = input("Enter the str value : ")

rev = ""

for i in string:
    rev = i + rev
print("Reversed string is : ", rev)

if (rev == string):
    print("The enterd string is a palindrome !")
else:
    print("The enterd string is not a palindrome")
