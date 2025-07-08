def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi:.2f}")
print("Category:", category(bmi))
