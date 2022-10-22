print("Weclome to the roller coaster")
height=int(input("What is your height in cm? "))
age=int(input("Enter your age "))
if height >= 120:
    print("You can ride the roller coaster!")
    if age<12:
        print("Please pay $5")
    elif age<=18:
        print("Please pay $7")
    else:
        print("Please pay $12")        
else:
   print("You have to grow taller before you ride.")
     