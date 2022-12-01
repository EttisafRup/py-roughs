user_age = int(input("Please tell us your age \n Age : "))
if (80 <= user_age) or (user_age <= 9) :
    print("Are you comedy me? 😂")
else :
    if user_age > 18:
        print("You are able to drive")
    elif user_age == 18:
        print("We cannot decided about your qualification. Please visit to us physically and bla bla")
    else :
        print("You are not able to drive, go and watch POGO")