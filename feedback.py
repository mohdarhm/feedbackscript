import random as number
import keyboard as kb
import time


# prac sect
subs=int(input("Enter Subs"))
fields=int(input("Enter # of fields"))

time.sleep(4)
for x in range(subs):
    for v in range(fields):
        g=number.randint(0,1)
        if g==1:
            for _ in range(2):
                kb.press_and_release("Down")
                time.sleep(0.5)
        else:
            for _ in range(5):
                kb.press_and_release("Down")
                time.sleep(0.5)
            
        kb.press_and_release("Tab")
    kb.write("No additional comments needed.")
    kb.press_and_release("Tab")
    time.sleep(0.75)

    kb.press_and_release("Tab")

