import random, easygui

secret = random.randint(1,99)
guess = 0;
tries = 0;

easygui.msgbox("""Hi, There is a secret!, It is a number from 1 to
99. I'll give you 6 tries.""")

while guess != secret and tries < 6:
    guess = easygui.integerbox("what's is your guess? ")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low")
    elif guess > secret:
        easygui.msgbox(str(guess) + "is too high")
    tries += 1

if guess == secret:
    easygui.msgbox("you got it! Congratulation you")
else:
    easygui.msgbox("no more guess! Better luck next time...")