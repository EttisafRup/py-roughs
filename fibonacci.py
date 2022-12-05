import sys
sys.setrecursionlimit(5000)


def function(number):
    """Hedar Doc"""
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return function(number - 1) + function(number + 2)


_ = int(input("De bhai number de"))
print(function(_))
