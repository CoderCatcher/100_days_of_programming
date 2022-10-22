number=input("Enter the two-digit-number")
tc=int(number)
first_digit=tc%10
second_digit=(tc-first_digit)/10
sum=first_digit+second_digit
print(sum)
