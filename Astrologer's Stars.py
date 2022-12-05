import os
os.system("clear")

print("\n\n 🖤😲 Astrologer's Stars Generator 😲🖤 \n\n")
i = 0
star_limit = int(input("Enter how many starts you want to pattern : \n"))

print("\n\n Your Pattern Style : \n 1. Column \n 2. Column-Reverse")
direction = bool(int(input("")))

if direction is True:
    print("Column Pattern of", star_limit, "stars \n")
    while i <= star_limit:
        print("*" * i)
        i += 1
elif direction is False:
    print("Column Reverse Pattern of", star_limit, "stars \n")
    while i <= star_limit:
        print("*" * star_limit)
        star_limit -= 1
else:
    print("Something went Wrong :/ ")
