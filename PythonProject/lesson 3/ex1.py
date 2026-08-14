name = input("What is your name?\n ")
weight = float(input("What is your weight in kilograms\n (for example: 82.5) "))
height = float(input("What is your height in meters?\n (for example: 1.79) "))

bmi = weight / (height ** 2)

bmi_round = int(round(bmi, 2))
bmi_type = type(bmi_round)

print(f"{name} is {weight} kilograms, his {height} meters and his {bmi_round} bmi, {bmi_type}.")

