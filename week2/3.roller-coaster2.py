print("Welcome to the roller coaster!")

height = int(input("Please enter your height in cm: "))

if height >= 120:
    print("You can ride the roller coaster.")
    
    age = int(input("Please enter your age: "))
    
    if age < 12:
        print("You need to pay $5.")
    elif age < 18:
        print("You need to pay $7.")
    else:
        print("You need to pay $12.")
        
else:
    print("Sorry, you must be at least 120 cm tall to ride.")
