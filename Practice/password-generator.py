import string
import random

global choice

try:
    passLength = int(input("Enter password length: "))
except KeyboardInterrupt:
    print("\nGoodbye! Program stopped by user.")
    exit()

def choosePassword() -> tuple:
    passVariaton = ["Digits", "Uppercase", "Lowercase", "Punctuation", "Done"]
    variation = []
    choice = 0    

    for i in range(len(passVariaton)):
        print(f"{i+1} - {passVariaton[i]}")

    while len(variation) < 4: 
        choice = int(input("Masukan pilihan (1/2/3/4/5): "))

        if passVariaton[choice-1].lower() in variation:
            print("You've already choose that variation")
            choice = 0

        if choice == 1:
            variation.append("digits")
        elif choice == 2:
            variation.append("uppercase")
        elif choice == 3:
            variation.append("lowercase")
        elif choice == 4:
            variation.append("punctuation")
        elif choice == 5:
            if len(variation) == 0:
                print("Atleast choose something first.")
            else:
                break

    return variation

def createPassword(variation: tuple, length: int) -> list:
    characterList = ""
    password = []

    if ("digits" in variation):
        characterList += string.digits
    if ("uppercase" in variation):
        characterList += string.ascii_uppercase
    if ("lowercase" in variation):
        characterList += string.ascii_lowercase
    if ("punctuation" in variation):
        characterList += string.punctuation

    for i in range(length):
        randomCharacter = random.choice(characterList)
        password.append(randomCharacter)

    return password

def main():
    passwordVariation = choosePassword()
    password = createPassword(passwordVariation, passLength)

    print("Your password is " + "".join(password))

if __name__ == "__main__":
    main()