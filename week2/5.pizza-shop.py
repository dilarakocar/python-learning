# Python Pizza Shop
# Choose your pizza size: S (Small), M (Medium), L (Large)
# Prices: S = $15, M = $20, L = $25
# Add pepperoni: +$2 (Small), +$3 (Medium/Large)
# Add extra cheese: +$1

print("Welcome to Pizza House!")

size = input("What size pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
else:
    print("Please choose a valid size (S, M, L).")

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}.")
