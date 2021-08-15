number = int(input("which multiplication table would you like? "))
high = int(input("how high do you want to go? "))
print("Here's your table:")
for i in range(1, high + 1):
    print(number, "*", i, "=", number * i)