import easygui

flavor = easygui.enterbox("what is your favorite ice cream?",
                          default="orange")
easygui.msgbox("you enterd " + flavor)
