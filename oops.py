import os
os.system("clear")


class Student:
    def __init__(self, studentName, studentAge, gender, studentClass):
        self.name = studentName
        self.age = studentAge
        self.gender = gender
        self.present_class = studentClass

    def playing(self):
        print(f"{self.name} is playing")

    def sleeping(self):
        print(f"{self.name} is sleeping")

    def studying(self):
        print(f"{self.name} is studying")


rup = Student("Rup", "16", "Male", "11")
tisha = Student("Tisha", "18", "Female", "11")

rup.studying()
