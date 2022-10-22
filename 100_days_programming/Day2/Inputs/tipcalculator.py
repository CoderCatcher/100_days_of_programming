print("Welcome to the tip calculator")
bill=float(input("Enter the total bill "))
tip=int(input("How much tip do you want to give? 10, 12, or 15? "))
people=int(input("How much people do you wanna split "))
total_bill=((tip/100)*bill)+bill
bill_per_person=total_bill/people
bill2=round(bill_per_person,2)
bill2="{:.2f}".format(bill2)
print(f"The amount each person has to pay= {bill2}")