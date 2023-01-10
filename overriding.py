# 1. Nijer Constructor er bhetore. Thakle Print, na thakle Error.
# 2. Inherited Class tar Parent class er Constructor niye thake (inherit kore thake). Nijer moddhe abar notun kore Constructor function bananor mane holo ager constructor function ta ke override kore dewa
#  3. Jodi Constructor e variable khuje na pay, then nijer Own Class Variables gulor bhetor khuje.
# 4. Jodi nijer Own Class Variables gulor bhetor khuje na pay, tahole Parent class er Class Variables gulor khuje.

# Dada Class
class One:
    variable_One_const = "Rup but out of constructor"
    variable_One = "Rup"

    def __init__(self):
        self.variable_One_const = "Rup but in constructor"


# Nati Class
class Two(One):
    # variable_One = "Tisha"
    variable_Two = "Rup"
    # variable_One_const = "Tisha but out of constructor"

    # Peddani/Ustadi kora
    def __init__(self):
        # Ghorar Anda
        pass


one = One()
two = Two()

print(two.variable_One_const)
