# => Faulty Calculator
import random 
first_input = int(input("First Number :"))
second_input = int(input("Second Number :"))
math_action = input("Math Action (+,-,*,/) : ")

black_listed_values = [46, 52, 48, 7, 9, 18]

if (first_input in black_listed_values) or (second_input in black_listed_values)  :
    print(first_input + second_input * random.randint(5,9))
else :
    if math_action == "+" :
        print(first_input + second_input )

    elif math_action == "-" :
        print(first_input - second_input )

    elif math_action == "*" :
        print(first_input * second_input )

    elif math_action == "/" :
        print(first_input / second_input )
    else :
        print("Ekdin marjayee ga :)")
