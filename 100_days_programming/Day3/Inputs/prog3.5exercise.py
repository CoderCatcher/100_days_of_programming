print('Welcome to the love Calculator')
n1=input("BF Name: ")
n2=input("Gf Name: ")
n=n1+n2
t=n.count('t')
r=n.count('r')
u=n.count('u')
e=n.count('e')
total=t+r+u+e
l=n.count('l')
o=n.count('o')
v=n.count('v')
e=n.count('e')
total=total*10+l+o+v+e
if total<10 or total>90:
    print(f"Your score is {total}, you go like cola and mentos.")
elif total>=40 and total <=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
