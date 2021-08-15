# @author: rmcgo
# @date: 2021/8/15

gender = input("please enter your gender: ")
if gender == "female":
    age = int(input("please enter your age: "))
    if 10 <= age <= 12:
        print("we hope you can join our ball team!")
    else:
        print("sorry, we only need age in 10 to 12 person, have a good time!")
else:
    print("sorry, we only need female girl, have a good time!")