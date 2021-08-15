# @author: rmcgo
# @date: 2021/8/15

size = float(input("size of tank? "))
percent = float(input("percent full? "))
kmPerLiter = float(input("km per liter? "))
distance = size * percent / 100 * kmPerLiter
print("you can go another", distance, "km")
print("the next gas station is 200km away")
if distance > 200:
    print("you can wait for the next station")
else:
    print("Get gas now!")