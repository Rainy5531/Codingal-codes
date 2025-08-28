height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("Your are underweight")
elif BMI <= 24.9:
    print("Your are healthy")
elif BMI <= 29.9:
    print("Your are overweight")
elif BMI <= 34.9:
    print("Your are severely overweight")
elif BMI <= 39.9:
    print("Your are obese")
else:
    print("Your are severely obese")