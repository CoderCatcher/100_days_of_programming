w=float(input("Enter your weight"))
h=float(input("Enter your height"))
bmi=float(w/h*h)
bmi=round(bmi,2)
if bmi<=18.5:
    print(f"Your BMI is {bmi} and you are underweight")
elif bmi<25:
    print(f"Your BMI is {bmi} and you are normal weight")    
elif bmi<30:
    print(f"Your BMI is {bmi} and you are overweight")   
elif bmi<35:
    print(f"Your BMI is {bmi} and you are obese")    
elif bmi>=35:
    print(f"Your BMI is {bmi} and you are clinically obese")
