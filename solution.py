print("welcome to day 3 pizza delivery bus")
size=(input("Which size pizza do u want? S, M or L: ")).upper()
pepperoni=(input("Do u want pepperoni on your pizza? Y or N: ")).upper()
cheese=(input("Do you want cheese on your pizza? Y or N: ")).upper()
bill=0
if size == "S":
    bill+=15
elif size =="M":
    bill+=20
elif size =="L":
    bill+=25
else:
    print("entre correct inputs.")
if pepperoni== "Y":
    if size =="S":
        bill+=2
    else:
        bill+=3
if cheese=="Y":
    bill+=1
print(f"your total bill is: {bill}.")









