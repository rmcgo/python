# @author: rmcgo
# @date: 2021/8/15

sellingPrice = float(input("What's price you buy? "))
if sellingPrice <= 10:
    sellingPrice *= 0.9
else:
    sellingPrice *= 0.8
print("you final need pay", sellingPrice)