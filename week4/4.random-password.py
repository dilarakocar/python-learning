password_list = []

for char in range(0, letter_count):
    password_list.append(random.choice(letters))

for symbol in range(0, symbol_count):
    password_list.append(random.choice(symbols))

for number in range(0, number_count):
    password_list.append(str(random.choice(numbers)))

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Generated password: {password}")
