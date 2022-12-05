import random
import os
def hero_page():
    print("GuessTheNumber 😲🔥!")
    print("\n 1. Start \n 2. Menu \n 3. Exit")
    choosed_option = int(input("\r \r Select Your Path :"))

    if choosed_option == 1:
        guess_the_number()
    elif choosed_option == 2:
        os.system("clear")
        print("No Menu Available right now!")
        back = int(input("0. Go Back : "))
        if back == 0:
            os.system("clear")
            hero_page()

    else:
        os.system("clear")
        print("\n \n Thanks for your time, see you soon 💛\n \n")

def guess_the_number():
    os.system("clear")
    number = random.randint(0, 99)
    turn = 0
    while True:
        turn += 1
        user_input = int(input("Enter a Number between 0-99 :"))

        if user_input > number:
            print("Number too big, please enter a number that is less than",
                  user_input, "\n")
            continue
        elif user_input < number:
            print(
                "Number too small, please enter a number that is greater than", user_input, "\n")
            continue
        else:
            print("\n\n Bang! You guessed it right!! Total turns :", turn, "\n")
            yes_or_no = input("Would you like to play it again? Y/N \n ")
            if yes_or_no.lower() == "y":
                os.system("clear")
                number = random.randint(0, 99)
                print("\n \n Game has been restarted!")
                print("Enjoy with guessTheNumber 🖤! \n \n")
                continue
            else:
                os.system("clear")
                print("\n \n Thanks for your time, see you soon 💛\n \n")
                break


hero_page()
