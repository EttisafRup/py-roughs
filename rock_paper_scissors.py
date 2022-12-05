import os
import random
os.system("clear")

# => Menu Items
print("\n\n🥌📃✂  Rock Paper Scissors! 😲🖤\n\n")


def rps_gamefunc():
    """Function that executes the Rock Paper Scissors Game!"""

    # ! ScoreBoard
    _userscore_ = 0
    _computerscore_ = 0
    _tiescore_ = 0

    # -> Emoji Setup
    attack_attr = ["🥌", "📃", "✂"]
    attack_countdown = 0

    while True:
        print("\n")
        print("Choose your Attack :\n 1. Rock (🥌) \n 2. Paper (📃) \n 3. Scissors (✂) \n\n")

        # => Computer Attack Attributes
        _computer_attack_ = random.randint(1, 3)
        # => User Attack Attributes
        _user_attack_ = int(input("\n🕶 Choose Attack : "))
        # => count_down Chance
        os.system("clear")

        attack_countdown += 1
        print("[😲🔥] Attack Count :", attack_countdown - 1, "\n\n")

        if attack_countdown > 10:
            print("    - Game Over 😪")
            print(
                f"\n ☕ Matches Played : 🔟 \n 🤖 Your Score : {_userscore_} \n 💻 Computer Score : {_computerscore_} \n 👔 Total Tie : {_tiescore_} \n\n")
            break

        if _user_attack_ == _computer_attack_:
            print("Your attack :", attack_attr[_user_attack_-1])
            print("Computer attack :", attack_attr[_computer_attack_-1])

            print("Ow ow, it's a tie! Try again! 😁")
            _tiescore_ += 1
            continue

        elif _user_attack_ == 1 and _computer_attack_ == 3 or _user_attack_ == 3 and _computer_attack_ == 2 or _user_attack_ == 2 and _computer_attack_ == 1:
            print("Your attack :", attack_attr[_user_attack_-1])
            print("Computer attack :", attack_attr[_computer_attack_-1])

            print("You won! 😲🔥")
            _userscore_ += 1
            continue

        elif _user_attack_ == 1 and _computer_attack_ == 2 or _user_attack_ == 2 and _computer_attack_ == 3 or _user_attack_ == 3 and _computer_attack_ == 1:
            print("Your attack :", attack_attr[_user_attack_-1])
            print("Computer attack :", attack_attr[_computer_attack_-1])

            print("You lose! 😣😥")
            _computerscore_ += 1
            continue


try:
    rps_gamefunc()
except:
    os.system("clear")
    print("Please give a number to select the attack!\n\n")
    rps_gamefunc()
