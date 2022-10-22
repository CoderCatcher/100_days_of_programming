print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
directions=input(f"You're at a cross road. Where do you want to go? Type'left' or 'right' ")
if(directions=='left' or directions=='Left'):
  b=input(f"You come to a lake. There is an island in the middle of the lakses. Type 'wait' to wait for a boat. Type 'swim' to swim across ")
  if(b=='wait'or b=='Wait'):
    door=input(f"Which door do you want to choose? Blue , Yellow , Red ")
    if(door=='blue'or door=='Blue'):
      print("You entered the room of fire Game over")
    elif(door=='yellow'or door=='Yellow'):
      print("You found the treasure You win")
    elif(door=='red'or door=='Red'):
      print("You got attacked by an angry trout Game over")  
  elif(b=="swim"or b=='Swim'):
    print("You got attacked by sea kings Game over")    
else:
  print("You feel into a hole Game Over")

