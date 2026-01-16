# Snake Water Gun
import random

gameMap = [
    ["Draw","Win","Lose"],
    ["Lose","Draw","Win"],
    ["Win","Lose","Draw"]
]
count = 0
while True:

    computer = int(random.randint(0,2))
    user = int(input("Enter any option from list: 1. Snake 2. Water 3.Gun 0.Exit: "))
    if user == 0:
        break
    result = gameMap[computer][user-1]
    print("The result is : ",result)
    if result == "Win":
        count+=1

print("Score: ",count)