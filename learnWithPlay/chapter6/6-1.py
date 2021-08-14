import easygui

flavor = easygui.choicebox("What is your favorite ice cream flavor?",
                           choices=["banana", "Chocolate", "Strawberry"])
easygui.msgbox("you picked " + flavor)
