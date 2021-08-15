import easygui

# user_response = easygui.msgbox("Hello rmcgo")
# print(user_response)
#
# float1 = easygui.msgbox("12.32")

# str = easygui.enterbox("enter string")
# print(str)
#
# int1 = easygui.integerbox()
# print(int1)
#
# float1 = easygui.enterbox("some float")
# print(type(float1))
# float2 = float(float1)
# print(type(float2))

gender = easygui.enterbox("what is your gender? ",
                 default="male")
easygui.msgbox("you choiced " + gender)

