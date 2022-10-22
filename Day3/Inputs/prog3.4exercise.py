size=input("The size of your pizza? S or M or L ")
t=input("Pepperoni or Extra Cheese? Y or N ")
bill=0
if(size=='S'):
 bill=15
 if t=='Y' :
    bill+=2
 elif t=='N':
    bill+=1
elif(size=='M'):
    bill=20
    if t=='Y' :
     bill+=3
    elif t=='N':
     bill+=1
elif(size=='L'):
    bill=25
    if t=='Y' :
     bill+=3
    elif t=='N':
     bill+=1
print(f"Your total bill ${bill}")



