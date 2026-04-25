# If BMI > 25: overweight, if between 18–25: normal, if below 18: underweight

print("Body Mass Index (BMI)")

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = round(weight / (height ** 2), 2)

gender = input("Enter your gender (female/male): ").lower()

print(f"BMI: {bmi}")

if gender == "male":
    if bmi > 25:
        print("Overweight")
    elif bmi > 18:
        print("Normal")
    else:
        print("Underweight")
else:
    if bmi > 20:
        print("Overweight")
    elif bmi > 16:
        print("Normal")
    else:
        print("Underweight")
