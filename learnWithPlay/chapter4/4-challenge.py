#use int() realize 4minus 5plus
number = float(input("enter a number: "))
num1 = number - int(number);
if num1 < 0.5:
    print(int(number))
elif num1 >= 0.5:
    print(int(number+1))