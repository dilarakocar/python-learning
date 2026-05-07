import random

name_list = ["Caglar", "Cemile", "Duru", "Ada", "Nurevsan"]

# Alternative method
print(f"The lucky person who will pay the bill is: {random.choice(name_list)}")

# Another method using randint
random_payer = random.randint(0, len(name_list) - 1)

print(f"The lucky person who will pay the bill is: {name_list[random_payer]}")
