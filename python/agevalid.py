# to calculate pupil age
pl = input("how old are you?")
pl = int(pl)
### SRC - If we are validating then we will need a while loop
### to keep asking until the answer is correct.

if pl < 19 and pl >= 10:
    print("valid age")
else:
    print("invalid input: enter a value from 11 to 18")

### SRC - Remember to keep using the programming conventions...
