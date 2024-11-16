import string
import random

string.

character = ""
passLength = int(input("Enter password length: "))


def choosePassword():
    passVariaton = ["Digits", "Uppercase", "Special Characters", "Done"]
    choice = []

    for i in range(len(passVariaton)):
        print(f"{i+1} - {passVariaton[i]}")

    while len(choice) < 4 or choice == 4: 
        choice = int(input("Masukan pilihan (1/2/3/4): "))

def createPassword():
    pass