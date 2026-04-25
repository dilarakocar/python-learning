print("Welcome to the tip calculator!")

bill=float(input("what is the total bill?\n$"))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15?\n%"))
sharing=int(input("How many people to split the bill?\n"))

total_bill_per_person=round((bill+bill*(tip/100))/sharing,2)

print(f"Each person should pay ${total_bill_per_person}")
