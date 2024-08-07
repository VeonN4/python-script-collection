import random


choice = random.choice("Kertas", "Gunting", "Batu")
userChoice = str(input("(Kertas, Gunting, Batu): "))

if choice == userChoice:
    print("Draw")
elif userChoice == "Batu" and choice == "kertas":
    print("You lose")