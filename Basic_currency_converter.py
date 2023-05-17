print("-"*50)
print("Basic Currency Converter----Indian Rupee to Dollar")
print("-"*50)

IND = eval(input("Enter amount in Indian Rupee: "))
convert_to_usd = lambda IND: IND * 0.012
USD = convert_to_usd(IND)

print("That is ", USD, "USD.")

