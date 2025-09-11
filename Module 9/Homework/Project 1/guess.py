import random

number = random.randint(1, 10)
count = 0

while True:
    input_number = int(input("Guess a number between 1 and 10: "))

    if input_number == number:
        print("Congratulations! You guessed the correct number. You guessed it on your", count + 1, "try.")
        break

    else:
        count += 1
        print(f"Your guess is incorrect. Would you like to guess again?")
        continue_ = input('Yes or No: ')
        if continue_.lower() == 'no'or continue_.lower() == 'No':
            print(f"The correct number was {number}. Better luck next time!")
            break