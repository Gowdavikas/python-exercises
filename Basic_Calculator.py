print("-"*50)
print("Basic Calculator")
print("-"*50)
num1 = int(input("Enter the first value :"))
operator = input("Enter the operator ")
num2 = int(input("Enter the second value :"))

if operator == '+':
    print("The addition is: ", num1 + num2)
elif operator == '-':
    print("The subracted value: ", num1 - num2)
elif operator == '*':
    print("The multiplied value: ", num1 * num2)
elif operator == '/':
    print("The Division value: ", num1 / num2)
else:
    print("Invalid operator")