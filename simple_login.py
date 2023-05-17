print("-" * 50)
print("Create Your New Account")
print("-" * 50)

username = input("Enter your name: ")
password = input("Enter your password: ")

print("Your account is created!")
print("-" * 50)

print("Login now !")

username2 = input("Enter your name: ")
password2 = input("Enter your password: ")

if username == username2 and password == password2:
    print("Logged into your account successfully!!! ")

else:
    print("Invalid username 0r password, please check")