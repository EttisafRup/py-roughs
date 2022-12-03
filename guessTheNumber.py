import random
import os
number = random.randint(0, 99)
turn = 0
while True:
    turn += 1
    user_input = int(input("Enter a Number between 0-99 :"))

    if user_input > number:
        print("Number too big, please enter a number that is less than", user_input)
        continue
    elif user_input < number:
        print("Number too small, please enter a number that is greater than", user_input)
        continue
    else:
        print("Bang! You guessed it right!! Total turns :", turn)
        yes_or_no = input("Would you like to play it again? Y/N \n ")
        if yes_or_no.lower() == "y":
            os.system("clear")
            number = random.randint(0, 99)
            print("\n \n Game has been restarted!")
            print("Enjoy with guessTheNumber 🖤! \n \n")
            continue
        else :
            break
