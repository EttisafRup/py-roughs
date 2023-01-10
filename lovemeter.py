import os
import random
os.system("clear")

while True:
    you = input(f"Lover \n >> ")
    crush = input(f"Crush \n >> ")

    randomPercentage = random.randint(0, 100)
    randomHeartMatch = str(randomPercentage) + "%"

    print(f"{you} and {crush}'s heart match is {randomHeartMatch}")

    input("\n\n Press enter to continue again...")
    os.system("clear")
