age = int(input("Enter your age: "))

if age >= 18:
    attendance = int(input("Enter the number of classes missed: "))
    
    attendance = 200 - attendance
    percentage = (attendance / 200) * 100

    if percentage >= 75:
        print("You are eligible to take the exam.")

    else:
        print("/nYou are not eligible to take the exam. \nAt least 75% attendace is required. \nYour current attendance is", percentage, "%.")

else:
    print("You are not eligible to take the exam. \nYou must be at least 18 years old to take the exam.")