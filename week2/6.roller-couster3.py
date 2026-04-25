print("Welcome to the roller coaster!")

height = int(input("Please enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster.")
    
    age = int(input("Please enter your age: "))
    
    if age < 12:
        print("Children under 12 pay $5.")
        bill = 5
    elif age < 18:
        print("Ages 12 to 17 pay $7.")
        bill = 7
    elif 45 <= age <= 55:
        print("Everything is going to be okay. Have a free ride!")
        bill = 0
    else:
        print("Adults pay $12.")
        bill = 12

    photo = input("Do you want a photo? Yes or No: ").lower()
    
    if photo == "yes":
        bill += 3

    print(f"Your total bill is ${bill}.")
else:
    print("Sorry, you must be at least 120 cm tall to ride.")
