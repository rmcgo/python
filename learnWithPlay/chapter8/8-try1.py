number = int(input("which multiplication table would you like?\n"))
print("Here's your table:")
for i in range(1, 11):
    print(number, "*", i, "=", number * i)
