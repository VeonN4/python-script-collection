import random

userScore = 0
botScore = 0

winCondition = 0

def userPrompt():
    print("\nGame")
    print("Kertas - Gunting - Batu")

    userChoice = input("Pilih (Kertas, Gunting, Batu): ")

    return userChoice


def game(userChoice: str, botChoice: str):
    if userChoice.lower().strip() == "kertas":
        match botChoice:
            case "Kertas":
                winCondition = 1
            case "Batu":
                winCondition = 0
            case "Gunting":
                winCondition = 0
    elif userChoice.lower().strip() == "gunting":
        match botChoice:
            case "Kertas":
                winCondition = 0
            case "Batu":
                winCondition = 1
            case "Gunting":
                winCondition = 0
    elif userChoice.lower().strip() == "batu":
        match botChoice:
            case "Kertas":
                winCondition = 0
            case "Batu":
                winCondition = 0
            case "Gunting":
                winCondition = 1

    return winCondition

def setScore(condition: int):
    global userScore
    global botScore

    if condition == 1:
        print("Kamu menang!\n")
        userScore += 1
    else:
        print("Kamu kalah!\n")
        botScore += 1

    print(f"Bot Score: {botScore}")
    print(f"User Score: {userScore}")

def main():
    choices = ["Kertas", "Gunting", "Batu"]
    userChoice = ""

    while userChoice.lower().strip() != "stop":
        botChoice = random.choice(choices)
        userChoice = userPrompt()
        condition = game(userChoice, botChoice)
        setScore(condition)

if __name__ == "__main__":
    main()

        
