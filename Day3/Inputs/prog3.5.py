print("Weclome to the roller coaster")
height=int(input("What is your height in cm? "))
age=int(input("Enter your age "))
n=0
if height >= 120:
    print("You can ride the roller coaster!")
    if age<12:
        print("Child tickets are $5")
        n=5
    elif age<=18:
        print("Young tickets are $7")
        n=7
    elif(age<=45 and age<=55):
        print("Everything is okay just ride with us")
    else:
        print("Adult tickets are $12")
        n=12 
    wants_photo=input("Do you want a photo been taken? Y or N.")
    if(wants_photo=="Y"):
       n+=3   
    print(f"Your total bill${n}")
else:
 print("You have to grow taller before you ride.")
