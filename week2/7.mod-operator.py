number = int(input("Enter a number: "))
divisor = int(input("Enter the divisor: "))

remainder = number % divisor
remainder_when_divided_by_2 = number % 2

print("Remainder:", remainder)
print("Remainder when divided by 2:", remainder_when_divided_by_2)

#Bonus

if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")
