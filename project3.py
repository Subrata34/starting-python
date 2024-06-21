import random 
DiceRolling =True
while DiceRolling :
    print(random.randint(1,6))
    playAgain=input("Do you want to Roll Again[Y/N]")
    if playAgain=="Y":
         continue
    else:
         break