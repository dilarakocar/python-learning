import random

name_list = []

person1 = input("Enter the 1st person at the table: ")
name_list.append(person1)

person2 = input("Enter the 2nd person at the table: ")
name_list.append(person2)

person3 = input("Enter the 3rd person at the table: ")
name_list.append(person3)

person4 = input("Enter the 4th person at the table: ")
name_list.append(person4)

random_payer = random.randint(0, len(name_list) - 1)

print(f"The lucky person who will pay the bill is: {name_list[random_payer]}")
