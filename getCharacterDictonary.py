import random
import os 
os.system("clear")
userInput = input("Which girl you want to know about? \n").lower()

rupCrushes = {
    "suchishmeeta" : "Rup's Noble Character based on love story",
    "praptika" : "Rup's Fake Identifier Girl",
    "anamika" : "Fictional Character",
    "anika" : "Fictional Character",
}


if userInput == "" :
    randomInteger = random.randint(0,3)
    character = list(rupCrushes)[randomInteger]
    print("Randomly Generated!")
    print(character.capitalize() + ",", rupCrushes[character] )
else:
    print(userInput.capitalize() + ",",  rupCrushes.get(userInput.lower()))